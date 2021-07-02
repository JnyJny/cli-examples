"""CLI built on sys.argv

"""

import sys


# called by the stub created by poetry from pyproject.toml
def main() -> None:
    """The main entry point for this command-line tool. 
    """
    print("example0", __file__)
    print(f"argv={sys.argv}")

    if '--help' in sys.argv:
      print("No help for you")
      exit()



# only needed if the file is executed directly
if __name__ == '__main__':
    main()
