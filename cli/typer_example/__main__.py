""" copy file implemented with typer
"""

import typer

cli = typer.Typer()


@cli.command(context_settings=dict(help_option_names=["--help", "-h"]))
def concatenate_files(
    input_file: typer.FileText = typer.Option("-"),
    output_file: typer.FileTextWrite = typer.Option("-"),
    flag: bool = False,
) -> None:
    """Copy input file to the named output file."""

    print("flag", flag)
    output_file.write(input_file.read())


if __name__ == "__main__":
    cli()
