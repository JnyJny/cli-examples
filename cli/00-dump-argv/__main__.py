""" introduction to sys.argv                                           
                                                                       
Prints the contents of sys.argv and exits with status 11               
"""

import sys

if __name__ == "__main__":
    for n, item in enumerate(sys.argv):
        print(f"argv[{n}] == {item}")
    exit(11)
