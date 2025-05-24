# 🌱 Quickclone

🛠️ A smart, friendly CLI tool for cloning GitHub repositories — with optional virtualenv setup, project indexing, and interactive prompts.

✨ **What It Does**

- Clones GitHub repos using a simple `user/project` format
- Prompts for confirmation, virtualenv setup, and indexing
- Detects Python projects (`requirements.txt` or `pyproject.toml`)
- Logs clone details in `clone_log.txt`
- Supports flags for full automation or dry runs
- Quits gracefully at any stage with `q`

---

## 🧰 Clone the Quickclone Repository to Your System

In your terminal, run:

```bash
git clone https://github.com/aalbrightpdx/quickclone.git
cd quickclone
```

# 🧰 Install

If you're using pipx (recommended):

```bash
pipx install .
```

# 🚀 Usage

Once installed, from any directory run:

```bash
quickclone              # Interactive mode
quickclone user/repo    # Clone with default options
quickclone --venv       # Also set up a Python virtualenv if needed
quickclone --dry-run    # Preview what would happen
quickclone -h           # Show help
```

🧪 Example Workflow:

```bash
📦 Repo to clone: username/gitproject
📁 Target folder: ./gitproject
✅ Proceed with cloning? [y/n/q]: y
🌀 Cloning...
🐍 Python project detected — create virtualenv? [y/n/q]: y
✅ Virtualenv created.
📚 Add to project index? [y/n/q]: n
📝 clone_log.txt created.
🎉 Done! Your project is ready.
```

# ❌ Uninstall

```bash
pip uninstall quickclone
```

# 💡 Requirements

Python 3.7+
Git installed and in your system PATH

# 📜 License

MIT — free to use, modify, and share.

🌿 For makers, tinkerers, and coders who want more than just a clone.
