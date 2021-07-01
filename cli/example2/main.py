"""
"""

import typer

cli = typer.Typer()

@cli.command()
def example2_command(title: str) -> None:
    print("example2", __file__)
    print(f"title={title}")

