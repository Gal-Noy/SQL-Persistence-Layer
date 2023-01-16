from persistence import *

import sys


def main(args: list[str]):
    input_file_name: str = args[1]
    with open(input_file_name) as input_file:
        for line in input_file:
            split_line: list[str] = line.strip().split(", ")
            # TODO: apply the action (and insert to the table) if possible


if __name__ == '__main__':
    main(sys.argv)
