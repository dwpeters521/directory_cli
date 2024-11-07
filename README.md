# directory_cli
A CLI for interacting with folders

# Summary

The purpose of this repository is to build a CLI for interacting with directories. Users will be able to enter commands to create, delete, move, and list directories in a sample file system. This app will not create actual directories, but rather maintain a stateful file system which can be listed, verifying the output of the user's commands

# Contributing

## Running the App
To run this application, you can use a Python virtual environment:

```bash
pyenv virtualenv directory_cli
pyenv activate directory_cli
```


And run the application from the `src` directory:

```bash
cd src
python directories.py
```

Please note that you can change the input to this tool by modifying the `commands` string in `app.py`
This tool currently assumes that the commands start each new line with no whitespace, and have an additional space before directory names:

```
commands = """
CREATE fruits
CREATE vegetables
CREATE fruits/apples
DELETE fruits/apples
...
"""
```

## Testing
If you wish to run the test suite, you may similarly run that file from the `src` directory:

```
python tests.py
```

## Future Work
That's it! If you wish to contribute, please feel free. Future work may include:
 - Support for additional commands
 - Better processing to allow for more flexible input
 - A real CLI