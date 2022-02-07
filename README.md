# cli-examples - Selection of Python CLI Implementations

## Installation

### Clone The Repo
1. `$ git clone https://github.com/JnyJny/cli-examples`
1. `$ cd cli-examples`

### Install with Poetry
1. `$ poetry shell`
1. `$ poetry install`


### Install with Pip
1. `$ python3 -m venv .venv`
1. `$ source .venv/bin/activate`
1. `$ python3 -m pip install -r requirements.txt`

--

## Introduction to `sys.argv`
The contents of `cli/00-dump-argv/__main__.py`:
```python
""" introduction to sys.argv

Prints the contents of sys.argv and exits with status 11
"""

import sys

if __name__ == "__main__":
    for n, item in enumerate(sys.argv):
        print(f"argv[{n}] == {item}")
    exit(11)
```

```console
$ python3 -m cli foo -bar ack -v

['/Users/ejo/local/cli-examples/cli/__main__.py', 'foo', '-bar', 'baz', '-v']
```
--

## Implementation of `cp` parsing `sys.argv`

The contents of `cli/10-argv/__main__.py`:

```python
""" copy file implemented with sys.argv
"""

import sys

if __name__ == "__main__":
    # default values
    inputfile = sys.stdin
    outputfile = sys.stdout
    flag = False

    # sys.argv[0] is the name of the program
    for ndx, item in enumerate(sys.argv[1:]):
        if item in ["-i", "--input-file"]:
            inputfile = open(sys.argv[ndx + 1], "r")
            continue
        if item in ["-o", "--output-file"]:
            outputfile = open(sys.argv[ndx + 1], "w")
            continue
        if item in ["-f", "--flag"]:
            flag = True
            continue
        if item in ["-h", "--help", "-?"]:
            print(
                sys.argv[0],
                "[--input-file name] [--output-file name] [--flag]",
                file=sys.stderr,
            )
            exit(1)
        raise ValueError(f"unexpected option {item}")

    print("flag", flag)

    outputfile.write(inputfile.read())
```

--

## Implementation of `cp` using `argparse`

The contents of `cli/20-argpase/__main__.py`:
```python
""" copy file implemented with argparse
"""


from argparse import ArgumentParser, FileType

if __name__ == "__main__":

    parser = ArgumentParser()
    parser.add_argument("--input-file", "-i", type=FileType("r"), default="-")
    parser.add_argument("--output-file", "-o", type=FileType("w"), default="-")
    parser.add_argument("--flag", "-f", action="store_true")
    args = parser.parse_args()

    print("flag", args.flag)

    args.output_file.write(args.input_file.read())
```

--


## Implementation of `cp` using `typer`

The contents of `cli/30-typer/__main__.py`:
```python
""" copy file implemented with typer
"""

import typer

cli = typer.Typer()

context_settings = dict(help_option_names=["--help", "-h"])


@cli.command(context_settings=context_settings)
def concatenate_files(
    input_file: typer.FileText = typer.Option("-"),
    output_file: typer.FileTextWrite = typer.Option("-"),
    flag: bool = False,
) -> None:
    """Copy input file to the named output file."""

    print("flag", flag)
    output_file.write(input_file.read())


if __name__ == "__main__":
    cli()

```

--


## Implementation of `cp` using `click`

```python
```

--



