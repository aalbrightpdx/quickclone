#!/usr/bin/env python3

import argparse
import subprocess
import os
import sys
import json
from datetime import datetime

# 🌿 Default config
project_index_file = os.path.expanduser("~/.quickclone_index.json")

def prompt(question, default=None):
    while True:
        answer = input(f"{question} ")
        if answer.lower() == 'q':
            print("👋 Exiting. See you next time!")
            sys.exit(0)
        if answer:
            return answer
        if default is not None:
            return default


def load_index():
    if os.path.exists(project_index_file):
        with open(project_index_file, 'r') as f:
            return json.load(f)
    return {}


def save_index(index):
    with open(project_index_file, 'w') as f:
        json.dump(index, f, indent=2)


def log_clone(path, repo_url):
    with open(os.path.join(path, "clone_log.txt"), "w") as f:
        f.write(f"Cloned from: {repo_url}\n")
        f.write(f"Date: {datetime.now().isoformat()}\n")


def setup_venv(path):
    print("🐍 Setting up virtual environment...")
    venv_path = os.path.join(path, "venv")
    subprocess.run(["python3", "-m", "venv", venv_path])
    print("✅ venv ready. To activate:")
    print(f"   source {os.path.relpath(venv_path)}/bin/activate")


def main():
    parser = argparse.ArgumentParser(
        description="🌱 quickclone - A friendly Git repo cloner",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("repo", nargs="?", help="GitHub repo in format user/project")
    parser.add_argument("--venv", action="store_true", help="Set up a Python virtualenv if applicable")
    parser.add_argument("--branch", type=str, help="Clone a specific branch")
    parser.add_argument("--index", action="store_true", help="Add to local project index")
    parser.add_argument("--dry-run", action="store_true", help="Preview the steps without cloning")
    parser.add_argument("--no-interactive", action="store_true", help="Skip interactive prompts")
    parser.add_argument("--target-dir", type=str, help="Custom target directory for the cloned project")

    args = parser.parse_args()

    if not args.repo and not args.no_interactive:
        args.repo = prompt("Enter GitHub repo (user/project):")

    if not args.repo:
        print("❌ Repo required.")
        return

    repo_url = f"https://github.com/{args.repo}.git"
    folder_name = args.repo.split("/")[-1]
    target_dir = args.target_dir or os.path.join(os.getcwd(), folder_name)

    if not args.no_interactive:
        print(f"📁 Target folder: {target_dir}")
        if prompt("Proceed with cloning here? (Y/n/q)", default="y").lower() != 'y':
            sys.exit(0)

    if os.path.exists(target_dir) and os.listdir(target_dir):
        print(f"❌ Target directory '{target_dir}' already exists and is not empty.")
        sys.exit(1)

    print("🌀 Cloning...")
    if not args.dry_run:
        try:
            cmd = ["git", "clone"]
            if args.branch:
                cmd += ["-b", args.branch]
            cmd += [repo_url, target_dir]
            subprocess.run(cmd, check=True)
        except subprocess.CalledProcessError as e:
            print(f"❌ Git clone failed: {e}")
            sys.exit(1)

        log_clone(target_dir, repo_url)

        if args.venv or (not args.no_interactive and prompt("Set up Python virtualenv if needed? (y/N/q)", default="n").lower() == 'y'):
            if os.path.exists(os.path.join(target_dir, "requirements.txt")) or \
               os.path.exists(os.path.join(target_dir, "pyproject.toml")):
                setup_venv(target_dir)
            else:
                print("⚠️  No Python project files detected. Skipping venv.")

        if args.index or (not args.no_interactive and prompt("Add to project index? (y/N/q)", default="n").lower() == 'y'):
            index = load_index()
            index[args.repo] = target_dir
            save_index(index)
            print("📚 Project added to index.")

    else:
        print(f"🌿 Dry run: would clone {repo_url} to {target_dir}")
        if args.branch:
            print(f"   with branch: {args.branch}")
        if args.venv:
            print("   would set up Python virtualenv")
        if args.index:
            print("   would add to project index")

    print("✨ Done. May your code compile on the first try.")


if __name__ == "__main__":
    main()

