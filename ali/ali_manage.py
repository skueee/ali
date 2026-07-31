import os
import subprocess
import sys
from pathlib import Path

from . import ali_module as ali


def get_commands_list(directory: Path):
    return [f.stem for f in directory.iterdir() if f.is_file()]

def list_commands():
    user_commands = get_commands_list(Path(f"{os.path.expanduser("~")}/.ali/bin/"))
    global_commands = get_commands_list(Path("/opt/ali/bin"))

    print('\033[0;34mUser commands :\033[0m')
    try:
        for i in user_commands:
            print(i)
    except TypeError:
        print("No command")
    print("\n")
    print('\033[0;34mGlobal commands :\033[0m')
    try:
        for i in global_commands:
            print(i)
    except TypeError:
        print("No command")

    sys.exit(0)

def get_command_path(command):
    if command in get_commands_list(Path(f"{os.path.expanduser("~")}/.ali/bin/")):
        return f"{os.path.expanduser("~")}/.ali/bin/{command}"
    elif command in get_commands_list(Path("/opt/ali/bin")):
        return f"/opt/ali/bin/{command}"

def main(command, action):
    if command == "list":
        list_commands()
    elif command in get_commands_list(Path(f"{os.path.expanduser("~")}/.ali/bin/")) or command in get_commands_list(Path("/opt/ali/bin/")):
        if action == "remove":
            try:
                os.remove(str(get_command_path(command)))
                sys.exit(0)
            except PermissionError:
                ali.get_sudo()
        elif action == "edit":
            subprocess.run(["nano", str(get_command_path(command))], check=False)
            sys.exit(0)
        else:
            print("Action not valid, try something else")
            sys.exit(1)
    else:
        print("Command not found in ali directories")
        sys.exit(1)
