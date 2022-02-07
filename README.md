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


## Introduction to sys.argv


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

Run this command with:

```


