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
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    1 """ introduction to sys.argv                                                    ┃
┃    2                                                                                 ┃
┃    3 Prints the contents of sys.argv and exits with status 11                        ┃
┃    4 """                                                                             ┃
┃    5                                                                                 ┃
┃    6 import sys                                                                      ┃
┃    7                                                                                 ┃
┃    8 if __name__ == "__main__":                                                      ┃
┃    9 │   for n, item in enumerate(sys.argv):                                         ┃
┃   10 │   │   print(f"argv[{n}] == {item}")                                           ┃
┃   11 │   exit(11)                                                                    ┃
┃   12                                                                                 ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```

```console
$ python3 -m cli foo -bar ack -v

['/Users/ejo/local/cli-examples/cli/__main__.py', 'foo', '-bar', 'baz', '-v']
```
--

## Implementation of `cp` parsing `sys.argv`

The contents of `cli/10-argv/__main__.py`:

```python
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    1 """ copy file implemented with sys.argv                                         ┃
┃    2 """                                                                             ┃
┃    3                                                                                 ┃
┃    4 import sys                                                                      ┃
┃    5                                                                                 ┃
┃    6 if __name__ == "__main__":                                                      ┃
┃    7 │   # default values                                                            ┃
┃    8 │   inputfile = sys.stdin                                                       ┃
┃    9 │   outputfile = sys.stdout                                                     ┃
┃   10 │   flag = False                                                                ┃
┃   11 │                                                                               ┃
┃   12 │   # sys.argv[0] is the name of the program                                    ┃
┃   13 │   for ndx, item in enumerate(sys.argv[1:]):                                   ┃
┃   14 │   │   if item in ["-i", "--input-file"]:                                      ┃
┃   15 │   │   │   inputfile = open(sys.argv[ndx + 1], "r")                            ┃
┃   16 │   │   │   continue                                                            ┃
┃   17 │   │   if item in ["-o", "--output-file"]:                                     ┃
┃   18 │   │   │   outputfile = open(sys.argv[ndx + 1], "w")                           ┃
┃   19 │   │   │   continue                                                            ┃
┃   20 │   │   if item in ["-f", "--flag"]:                                            ┃
┃   21 │   │   │   flag = True                                                         ┃
┃   22 │   │   │   continue                                                            ┃
┃   23 │   │   if item in ["-h", "--help", "-?"]:                                      ┃
┃   24 │   │   │   print(                                                              ┃
┃   25 │   │   │   │   sys.argv[0],                                                    ┃
┃   26 │   │   │   │   "[--input-file name] [--output-file name] [--flag]",            ┃
┃   27 │   │   │   │   file=sys.stderr,                                                ┃
┃   28 │   │   │   )                                                                   ┃
┃   29 │   │   │   exit(1)                                                             ┃
┃   30 │   │   raise ValueError(f"unexpected option {item}")                           ┃
┃   31 │                                                                               ┃
┃   32 │   print("flag", flag)                                                         ┃
┃   33 │                                                                               ┃
┃   34 │   outputfile.write(inputfile.read())                                          ┃
┃   35                                                                                 ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```

--

## Implementation of `cp` using `argparse`

The contents of `cli/20-argpase/__main__.py`:
```python
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    1 """ copy file implemented with argparse                                         ┃
┃    2 """                                                                             ┃
┃    3                                                                                 ┃
┃    4                                                                                 ┃
┃    5 from argparse import ArgumentParser, FileType                                   ┃
┃    6                                                                                 ┃
┃    7 if __name__ == "__main__":                                                      ┃
┃    8 │                                                                               ┃
┃    9 │   parser = ArgumentParser()                                                   ┃
┃   10 │   parser.add_argument("--input-file", "-i", type=FileType("r"), default="-")  ┃
┃   11 │   parser.add_argument("--output-file", "-o", type=FileType("w"), default="-") ┃
┃   12 │   parser.add_argument("--flag", "-f", action="store_true")                    ┃
┃   13 │   args = parser.parse_args()                                                  ┃
┃   14 │                                                                               ┃
┃   15 │   print("flag", args.flag)                                                    ┃
┃   16 │                                                                               ┃
┃   17 │   args.output_file.write(args.input_file.read())                              ┃
┃   18                                                                                 ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```

--


## Implementation of `cp` using `typer`

The contents of `cli/30-typer/__main__.py`:
```python
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    1 """ copy file implemented with typer                                            ┃
┃    2 """                                                                             ┃
┃    3                                                                                 ┃
┃    4 import typer                                                                    ┃
┃    5                                                                                 ┃
┃    6 cli = typer.Typer()                                                             ┃
┃    7                                                                                 ┃
┃    8 context_settings = dict(help_option_names=["--help", "-h"])                     ┃
┃    9                                                                                 ┃
┃   10                                                                                 ┃
┃   11 @cli.command(context_settings=context_settings)                                 ┃
┃   12 def concatenate_files(                                                          ┃
┃   13 │   input_file: typer.FileText = typer.Option("-"),                             ┃
┃   14 │   output_file: typer.FileTextWrite = typer.Option("-"),                       ┃
┃   15 │   flag: bool = False,                                                         ┃
┃   16 ) -> None:                                                                      ┃
┃   17 │   """Copy input file to the named output file."""                             ┃
┃   18 │                                                                               ┃
┃   19 │   print("flag", flag)                                                         ┃
┃   20 │   output_file.write(input_file.read())                                        ┃
┃   21                                                                                 ┃
┃   22                                                                                 ┃
┃   23 if __name__ == "__main__":                                                      ┃
┃   24 │   cli()                                                                       ┃
┃   25                                                                                 ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```

--


## Implementation of `cp` using `click`

```python
```

--



