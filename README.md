# Command Line Interface Examples in Python

A selection of CLI example code in Python that demonstrate different ways a program can get input from the user directly from the command line. 

- cli/example0 uses [`sys.argv`][argv]
- cli/example1 uses [`argparse.ArgumentParser`][argparse]
- cli/example2 uses [`typer`][typer]

After the package is installed, three command line tools will be available; `cli0`, `cli1` and `cli2`. 

## Install

This project is managed by `poetry` but can be installed locally using the following (I suggest installing into a virtual environment to minimize any side-effects on your existing Python installation). 

```
$ python3 -m venv .venv
$ source .venv/bin/activate
$ python3 -m pip install git+https://github.com/JnyJny/cli-examples
...
```
This only installs the example commands and not the source code for the project. See the **Develop** section for more information.

## Develop

The dependencies and packaging for this code is managed by the excellent tool [`poetry`][poetry] and I highly recommend learning how to use it. `Poetry` is much easier to use and manage than older techniques, such as `setup.py` and `setup.conf`. There are other modern packaging tools like `flit`, however I really like using `poetry`. 

```
$ python3 -m pip install poetry
```

After installing `poetry`, clone the repo:

```
$ git clone https://github.com/JnyJny/cli-examples
$ cd cli-examples
```

Next, start a `poetry` shell which will create and manage a virtual environment for you.

```
$ poetry shell
...
```

The first time after you've created a new virtual environment (typically after starting the shell the first time), you'll need to install the package and dependencies.

```
$ poetry install
...
```

Once this is complete, the three `cli` commands will become available and any edits you make to the source code will be "live" for those commands.


[argv]: https://docs.python.org/3/library/sys.html?highlight=argv#sys.argv
[argparse]: https://docs.python.org/3/library/argparse.html
[typer]: https://typer.tiangolo.com
[poetry]: https://python-poetry.org/docs/