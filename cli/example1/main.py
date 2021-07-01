"""
"""

from argparse import ArgumentParser


def main() -> None:
    """
    """
    print("example1", __file__)
    parser = ArgumentParser()
    parser.add_argument("--title", "-t", help="A book title")

    results = parser.parse_args()
    print(results)

if __name__ == "__main__":
    main()
