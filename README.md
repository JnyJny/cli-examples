# cli-examples
A selection of CLI example code in Python


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
The contents of `cli/__main__.py`:
```python
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    1 """ introduction to sys.argv                                            ┃
┃    2                                                                         ┃
┃    3 Prints the contents of sys.argv and exits with status 11                ┃
┃    4 """                                                                     ┃
┃    5                                                                         ┃
┃    6 import sys                                                              ┃
┃    7                                                                         ┃
┃    8 if __name__ == "__main__":                                              ┃
┃    9 │   print(sys.argv)                                                     ┃
┃   10 │   exit(11)                                                            ┃
┃   11                                                                         ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```

```console
$ python3 -m cli foo -bar ack -v

['/Users/ejo/local/cli-examples/cli/__main__.py', 'foo', '-bar', 'baz', '-v']
```
--

## Implementation of `cp` parsing `sys.argv`

The contents of `cli/example0/__main__.py`:

```python
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    1 """ copy file implemented with sys.argv                                 ┃
┃    2                                                                         ┃
┃    3 usage:  cp0 [-i input] [-o output] [-f]                                 ┃
┃    4 """                                                                     ┃
┃    5                                                                         ┃
┃    6 import sys                                                              ┃
┃    7                                                                         ┃
┃    8 if __name__ == "__main__":                                              ┃
┃    9 │   # default values                                                    ┃
┃   10 │   inputfile = sys.stdin                                               ┃
┃   11 │   outputfile = sys.stdout                                             ┃
┃   12 │   flag = False                                                        ┃
┃   13 │                                                                       ┃
┃   14 │   # sys.argv[0] is the name of the program                            ┃
┃   15 │   for ndx, item in enumerate(sys.argv[1:]):                           ┃
┃   16 │   │   if item in ["-i", "--input-file"]:                              ┃
┃   17 │   │   │   inputfile = open(sys.argv[ndx + 1], "r")                    ┃
┃   18 │   │   │   continue                                                    ┃
┃   19 │   │   if item in ["-o", "--output-file"]:                             ┃
┃   20 │   │   │   outputfile = open(sys.argv[ndx + 1], "w")                   ┃
┃   21 │   │   │   continue                                                    ┃
┃   22 │   │   if item in ["-f", "--flag"]:                                    ┃
┃   23 │   │   │   flag = True                                                 ┃
┃   24 │   │   │   continue                                                    ┃
┃   25 │   │   if item in ["-h", "--help", "-?"]:                              ┃
┃   26 │   │   │   print(                                                      ┃
┃   27 │   │   │   │   sys.argv[0],                                            ┃
┃   28 │   │   │   │   "[--input-file name] [--output-file name] [--flag]",    ┃
┃   29 │   │   │   │   file=sys.stderr,                                        ┃
┃   30 │   │   │   )                                                           ┃
┃   31 │   │   │   exit(1)                                                     ┃
┃   32 │   │   raise ValueError(f"unexpected option {item}")                   ┃
┃   33 │                                                                       ┃
┃   34 │   print("flag", flag)                                                 ┃
┃   35 │                                                                       ┃
┃   36 │   outputfile.write(inputfile.read())                                  ┃
┃   37                                                                         ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```

--

## Implementation of `cp` using `argparse`

The contents of `cli/example1/__main__.py`:
```python
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    1 """ copy file implemented with argparse                                 ┃
┃    2                                                                         ┃
┃    3 usage: cp1 [-i input] [-o output] [-f]                                  ┃
┃    4 """                                                                     ┃
┃    5                                                                         ┃
┃    6                                                                         ┃
┃    7 from argparse import ArgumentParser, FileType                           ┃
┃    8                                                                         ┃
┃    9 if __name__ == "__main__":                                              ┃
┃   10 │                                                                       ┃
┃   11 │   parser = ArgumentParser()                                           ┃
┃   12 │   parser.add_argument("--input-file", "-i", type=FileType("r"),       ┃
┃      default="-")                                                            ┃
┃   13 │   parser.add_argument("--output-file", "-o", type=FileType("w"),      ┃
┃      default="-")                                                            ┃
┃   14 │   parser.add_argument("--flag", "-f", action="store_true")            ┃
┃   15 │   args = parser.parse_args()                                          ┃
┃   16 │                                                                       ┃
┃   17 │   print("flag", args.flag)                                            ┃
┃   18 │                                                                       ┃
┃   19 │   args.output_file.write(args.input_file.read())                      ┃
┃   20                                                                         ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```


--


## Implementation of `cp` using `typer`

The contents of `cli/example2/__main__.py`:
```python
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    1 """ copy file implemented with typer                                    ┃
┃    2                                                                         ┃
┃    3 usage: cp2 [-i input] [-o output] [-f]                                  ┃
┃    4 """                                                                     ┃
┃    5                                                                         ┃
┃    6 import typer                                                            ┃
┃    7                                                                         ┃
┃    8 cli = typer.Typer()                                                     ┃
┃    9                                                                         ┃
┃   10                                                                         ┃
┃   11 @cli.command()                                                          ┃
┃   12 def concatenate_files(                                                  ┃
┃   13 │   input_file: typer.FileText = typer.Option("-"),                     ┃
┃   14 │   output_file: typer.FileTextWrite = typer.Option("-"),               ┃
┃   15 │   flag: bool = False,                                                 ┃
┃   16 ) -> None:                                                              ┃
┃   17 │   """Copy input file to the named output file."""                     ┃
┃   18 │                                                                       ┃
┃   19 │   print("flag", flag)                                                 ┃
┃   20 │   output_file.write(input_file.read())                                ┃
┃   21                                                                         ┃
┃   22                                                                         ┃
┃   23 if __name__ == "__main__":                                              ┃
┃   24 │   cli()                                                               ┃
┃   25                                                                         ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```

--


## Implementation of `cp` using `click`

--



