# directory_cli
A CLI for interacting with folders

# Summary

The purpose of this repository is to build a CLI for interacting with directories. Users will be able to enter commands to create, delete, move, and list directories in a sample file system. This app will not create actual directories, but rather maintain a stateful file system which can be listed, verifying the output of the user's commands

# Contributing

To run this application, you can use a Python virtual environment:

```bash
pyenv virtualenv directory_cli
pyenv activate directory_cli
```

Install basic requirements:

```bash
pip install -r requirements.txt
```


And run the application from the `src` directory:

```bash
cd src
python directories.py
```
