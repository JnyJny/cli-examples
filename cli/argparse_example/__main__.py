""" copy file implemented with argparse
"""


from argparse import ArgumentParser, FileType


def main() -> None:
    parser = ArgumentParser()
    parser.add_argument("--input-file", "-i", type=FileType("r"), default="-")
    parser.add_argument("--output-file", "-o", type=FileType("w"), default="-")
    parser.add_argument("--flag", "-f", action="store_true")
    args = parser.parse_args()

    print("flag", args.flag)

    args.output_file.write(args.input_file.read())


if __name__ == "__main__":
    main()
