import sys
import argparse


def cmd_help():
    return ""


def check_args(args):
    return True


def argparse_init():
    my_parser = argparse.ArgumentParser(
        prog="updateip",
        usage="%(prog)s [options]",
        description="Software to handle AWS security groups",
        allow_abbrev=False,
        formatter_class=argparse.RawTextHelpFormatter)

    my_parser.add_argument(
        '-f',
        '--file',
        dest='file',
        help='Get AWS config file',
        required=True,
        type=str
    )

    my_parser.add_argument(
        '-d',
        '--domain-name',
        dest='domain_name',
        type=str,
        help="Domain name to resolve as IP address",
    )

    my_parser.add_argument(
        '-i',
        '--ip',
        dest='ip_address',
        type=str,
        help="IP address",
    )

    args = my_parser.parse_args()

    if not check_args(args):
        my_parser.print_help()
        return None

    if len(sys.argv) <= 1:
        my_parser.print_help()
        return None

    if not args:
        print("Error in arguments")
        my_parser.print_help()
        return None

    return args
