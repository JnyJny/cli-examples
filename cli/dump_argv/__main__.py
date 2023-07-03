""" introduction to sys.argv                                           
                                                                       
Prints the contents of sys.argv and exits with status 11               
"""

# from cli.dump_argv.__main__ import main as main_dump_argv

import sys


def main() -> None:
    for n, item in enumerate(sys.argv):
        print(f"argv[{n}] == {item}")
    exit(11)


if __name__ == "__main__":
    main()
