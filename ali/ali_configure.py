import os
import pwd
import subprocess
import sys
from pathlib import Path

from . import ali_module as ali

def get_user_shell():
    print("What shell you are using?")
    print("1. bash (default)")
    print("2. fish")
    shell = input(": ")
    if shell == "1":
        return "bash"
    elif shell == "2":
        return "fish"
    else:
        print("Invalid option. Defaulting to bash.")
        return "bash"

def add_to_path(directory, shell):
    if shell == "bash":
        export_line = f'\nexport PATH="$PATH:{directory}"\n'

        with open(Path("/etc/bash.bashrc"), "a+") as file:
            file.seek(0)
            if directory not in file.read():
                file.write(export_line)
                print("Folder added to PATH in ~/.bashrc")
            else:
                print("Folder already in PATH")
    elif shell == "fish":
        try:
            subprocess.run(["fish", "-c", f"fish_add_path {directory}"], check=True)
        except FileNotFoundError:
            print("Fish shell not found. Please install fish shell to use this feature.")
        except subprocess.CalledProcessError as e:
            if e.returncode == 1:
                print("Directory is already in the PATH for fish shell.")
            else:
                print(f"An error occurred while trying to add the directory to the PATH in fish shell. Exit Code = {e.returncode}")

def create_dir(directory):
    try:
        os.mkdir(directory)
    except FileExistsError:
        print('\033[38;5;208mWarning: Directory already exists\033[0m')
    except PermissionError:
        print('\033[31mPermission denied: Unable to create the directory.\033[0m')

def check_if_line_in_file(linelist, line):
    found = False
    for x in linelist:
        if line in x:
            found = True
            return True
    if not found:
        return False

def is_configured():
    with open('/etc/bash.bashrc', 'r') as f:
        linelist = f.readlines()
    local_status = check_if_line_in_file(linelist, 'export PATH="$PATH:~/.ali/bin"')
    global_status = check_if_line_in_file(linelist, 'export PATH="$PATH:/opt/ali/bin"')

    return bool(local_status and global_status)

def configure():
    ali.get_sudo()
    shell = get_user_shell()

    user_info = pwd.getpwnam(str(os.environ.get("SUDO_USER")))
    create_dir("/opt/ali/")
    create_dir("/opt/ali/bin/")
    add_to_path("/opt/ali/bin/", shell)
    create_dir(f"{pwd.getpwnam(str(os.environ.get("SUDO_USER"))).pw_dir}/.ali/")
    os.chown(Path(f"{pwd.getpwnam(str(os.environ.get("SUDO_USER"))).pw_dir}/.ali/"), user_info.pw_uid, user_info.pw_gid)
    create_dir(f"{pwd.getpwnam(str(os.environ.get("SUDO_USER"))).pw_dir}/.ali/bin/")
    os.chown(Path(f"{pwd.getpwnam(str(os.environ.get("SUDO_USER"))).pw_dir}/.ali/bin"), user_info.pw_uid, user_info.pw_gid)
    add_to_path("~/.ali/bin", shell)

    print('Ali is configured !\nTo create your first command, run ali create [command name] ["command"]')
    sys.exit()
