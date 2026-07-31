import os
import sys
from pathlib import Path

from . import ali_configure as configure
from . import ali_module as ali


def get_path(is_global):
    if not is_global:
        return f"{os.path.expanduser("~")}/.ali/"
    else:
        return "/opt/ali/"

def main(is_global, command_name, command):
    if not configure.is_configured():
        print('You should execute "ali configure" first')
        sys.exit(1)

    if is_global:
        ali.get_sudo()

    path = get_path(is_global)

    if not os.path.isdir(Path(path)):
        os.mkdir(Path(path))

    try:
        with open(f"{path}bin/{command_name}", 'x') as f:
            f.write(command)
    except FileExistsError:
        print("The command already exists !")
        sys.exit(0)

    os.chmod(
        f"{path}bin/{command_name}",
        os.stat(f"{path}bin/{command_name}").st_mode | 0o555,
    )

    print("Done, you can now execute the command !\nTo manage it, execute ali manage [command] [remove/edit]")
    sys.exit(0)
