from persistence import *

import sys


def main(args: list[str]):
    input_file_name: str = args[1]
    with open(input_file_name) as input_file:
        for line in input_file:
            split_line: list[str] = line.strip().split(", ")
            curr_quantity = int(repo.execute_command(f"SELECT quantity FROM products where id = {split_line[0]}")[0][0])
            quantity_diff = int(split_line[1])
            if quantity_diff > 0 or (quantity_diff < 0 and curr_quantity >= quantity_diff):
                repo.execute_command(f"UPDATE products SET quantity = {curr_quantity + quantity_diff} WHERE id = {split_line[0]}")
                repo.tables_daos['Activities'].insert(Activitie(*split_line))


if __name__ == '__main__':
    main(sys.argv)
