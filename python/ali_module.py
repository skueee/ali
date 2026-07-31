import os
import sys


def get_sudo(exit = True):
    if os.getuid() != 0:
        if exit:
            print('\033[31mYou need root access to do that :(\033[0m')
            sys.exit(1)
        else:
            return False
    else:
        return True
