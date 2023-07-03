""" copy file implemented with click
"""

import click


@click.command()
@click.option("input-file", type=click.File("r"))
@click.option("output-file", type=click.File("w"))
def copy_files(input_file, output_file, flag):
    """Copy input file to the named output file."""
    print("flag", flag)

    output_file.write(input_file.read())


if __name__ == "__main__":
    copy_files()
