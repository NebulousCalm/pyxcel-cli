import typer


def warn(text: str) -> None:
    typer.echo(typer.style(text, fg=typer.colors.YELLOW))


def error(text: str) -> None:
    typer.echo(typer.style(text, fg=typer.colors.RED))
