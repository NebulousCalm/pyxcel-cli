import os
import subprocess
import sys


def update_() -> None:
    """
    Update the project
    :return:  none
    """

    install_dependencies('requirements.txt')
    update_dependencies('requirements.txt')


def install_dependencies(requirements_file: str) -> bool:
    """
    Installs necessary dependencies from the requirements file.

    :param requirements_file: requirements.txt file
    :return:  bool
    """
    try:
        subprocess.Popen(['pip', 'install', '-r', requirements_file], shell=True)
        return True
    except subprocess.CalledProcessError:
        return False


def update_dependencies(requirements_file: str) -> bool:
    """
    Updates necessary dependencies from the requirements file.
    :param requirements_file: requirements.txt file
    :return:  bool
    """
    try:
        with open(requirements_file, 'r') as file:
            packages = file.readlines()

        upgrade_packages = [pkg.strip() + " --upgrade" for pkg in packages]

        for package in upgrade_packages:
            subprocess.Popen([sys.executable, "-m", "pip", "install", package], shell=True)

        return True
    except subprocess.CalledProcessError as e:
        return False


def does_command_exist(command: str) -> bool:
    return os.path.exists('./commands/' + command)
