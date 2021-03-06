""" copy file implemented with sys.argv
"""

import sys


def main() -> None:
    inputfile = sys.stdin
    outputfile = sys.stdout
    flag = False

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


if __name__ == "__main__":
    main()
