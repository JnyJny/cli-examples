"""CLI using sys.argv

"""

import sys


# called by the stub created by poetry from pyproject.toml
def main() -> None:
    """
    """
    print("example0", __file__)
    print(f"argv={sys.argv}")


# only needed if the file is executed directly
if __name__ == '__main__':
    main()
