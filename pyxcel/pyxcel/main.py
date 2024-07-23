import typer
from typing_extensions import Annotated
from importlib import import_module
from pathlib import Path


from text_highlighting import warn_, error
from utils import does_command_exist, update_


def main(
        command: str = typer.Argument(..., help="Command to execute"),
        warn: bool = True
) -> None:

    if not warn: warn_('Running in \'no-warn\' this may have unforeseen consequences...')

    if command:
        if does_command_exist(command):
            try:
                # Dynamically import the command module
                command_module = import_module(f"commands.{command}")
                # Retrieve the function from the module
                command_func = getattr(command_module, command)
                # Execute the command function
                command_func(warn)
            except (ModuleNotFoundError, AttributeError) as e:
                error(f"Command '{command}' not found. Ensure the command file and function are named correctly.")
        else:
            error(f"Command '{command}' does not exist.")


if __name__ == "__main__":
    typer.run(main)
