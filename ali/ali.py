import argparse

from . import ali_configure as configure
from . import ali_create as create
from . import ali_manage as manage


def main():
    parser = argparse.ArgumentParser(
                        prog='ali',
                        description='A script to create "aliases" for long commands',
                        )

    parser.add_argument('arg1')
    parser.add_argument('arg2', nargs='?', default=None)
    parser.add_argument('arg3', nargs='?', default=None)
    parser.add_argument('-g', '--global', dest="is_global", action='store_true')

    args = parser.parse_args()

    if args.arg1 == "create":
        create.main(args.is_global, args.arg2, args.arg3)
    elif args.arg1 == "manage":
        manage.main(args.arg2, args.arg3)
    elif args.arg1 == "configure":
        configure.configure()
    else:
        print("This command does not exist")

if __name__ == "__main__":
    main()
