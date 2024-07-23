import typer
from typing_extensions import Annotated

from text_highlighting import warn, error
from utils import does_command_exist, update_


def main(
        command: str = "",

        update: Annotated[
            bool,
            typer.Argument(
                help="Updates necessary dependencies for this program"
            )
        ] = False,

        nowarn: Annotated[
            bool,
            typer.Argument(
                help="Runs all commands for this instance without warning notifications or preventions"
            )
        ] = False
):
    """
    pyxcel-cli made and maintained by [Zachary Richman](https://github.com/NebulousCalm)

    built using the incredible [typer](https://github.com/tiangolo/typer)
    """
    if update:
        update_()

    if nowarn:
        warn('Running in \'nowarn\' this may have unforeseen consequences...')

    if command:
        if does_command_exist(command):
            pass
        else:
            error('Command \'{}\' does not exist.'.format(command))
            raise typer.Exit(code=1)


if __name__ == '__main__':
    typer.run(main)
