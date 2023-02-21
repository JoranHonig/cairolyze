import click


@click.command()
def cairolyze():
    """Analyze cairo contracts
    """
    click.echo("Analysis done!")


if __name__ == "__main__":
    cairolyze()
