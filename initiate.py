from persistence import *

import sys
import os


def add_branche(split_line: list[str]):
    repo.branches_dao.insert(Branche(*split_line))


def add_supplier(split_line: list[str]):
    repo.suppliers_dao.insert(Supplier(*split_line))


def add_product(split_line: list[str]):
    repo.products_dao.insert(Product(*split_line))


def add_employee(split_line: list[str]):
    repo.employees_dao.insert(Employee(*split_line))


adders = {"B": add_branche,
          "S": add_supplier,
          "P": add_product,
          "E": add_employee}


def main(args: list[str]):
    input_file_name = args[1]

    # delete the database file if it exists
    repo._close()
    if os.path.isfile("bgumart.db"):
        os.remove("bgumart.db")

    repo.__init__()
    repo.create_tables()
    with open(input_file_name) as input_file:
        for line in input_file:
            split_line: list[str] = line.strip().split(",")
            adders.get(split_line[0])(split_line[1:])


if __name__ == '__main__':
    main(sys.argv)
