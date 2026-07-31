import os
import pwd
import shutil
import stat
import subprocess
import sys
from pathlib import Path

import ali_module as ali

def add_to_path(directory):
    export_line = f'\nexport PATH="$PATH:{directory}"\n'

    with open(Path("/etc/bash.bashrc"), "a+") as file:
        file.seek(0)
        if directory not in file.read():
            file.write(export_line)
            print("Folder added to PATH in ~/.bashrc")
        else:
            print("Folder already in PATH")

def create_dir(directory):
    try:
        os.mkdir(directory)
    except FileExistsError:
        print('\033[38;5;208mWarning: Directory already exists\033[0m')
    except PermissionError:
        print('\033[31mPermission denied: Unable to create the directory.\033[0m')

def is_configured():
    return os.path.isfile(Path("/etc/profile.d/ali.sh"))

def configure():
    ali.get_sudo()

    shutil.copy('userd-template.sh', '/etc/profile.d/ali.sh')

    st = os.stat('/etc/profile.d/ali.sh')
    os.chmod('/etc/profile.d/ali.sh', st.st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)

    user_info = pwd.getpwnam(os.environ.get("SUDO_USER"))
    create_dir("/opt/ali/")
    create_dir("/opt/ali/bin/")
    add_to_path("/opt/ali/bin")
    create_dir(f"{pwd.getpwnam(os.environ.get("SUDO_USER")).pw_dir}/.ali/")
    os.chown(Path(f"{pwd.getpwnam(os.environ.get("SUDO_USER")).pw_dir}/.ali/"), user_info.pw_uid, user_info.pw_gid)
    create_dir(f"{pwd.getpwnam(os.environ.get("SUDO_USER")).pw_dir}/.ali/bin/")
    os.chown(Path(f"{pwd.getpwnam(os.environ.get("SUDO_USER")).pw_dir}/.ali/bin"), user_info.pw_uid, user_info.pw_gid)
    add_to_path(f"{pwd.getpwnam(os.environ.get("SUDO_USER")).pw_dir}/.ali/bin")
    print("Directories created !")

    subprocess.call(['/bin/bash', '/etc/profile.d/ali.sh'])
    print("Path edited !")

    sys.exit()
