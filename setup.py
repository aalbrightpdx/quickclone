# setup.py

from setuptools import setup

setup(
    name='quickclone',
    version='0.1.0',
    py_modules=['quickclone'],
    entry_points={
        'console_scripts': [
            'quickclone=quickclone:main',
        ],
    },
    install_requires=[],
    author='Aaron Albright',
    description='🌱 A friendly GitHub repo cloner with prompts, venv setup, and indexing.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/aalbrightpdx/quickclone',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)

