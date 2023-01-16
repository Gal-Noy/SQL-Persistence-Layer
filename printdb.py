from persistence import *


def main():
    print_tables()
    detailed_employees_report()
    detailed_activities_report()


def print_tables():
    for table_name in repo.tables_daos.keys():
        print(table_name)
        for record in repo.tables_daos[table_name].find_all_sorted():
            print(record)


def detailed_employees_report():
    print('\nEmployees report')
    for record in repo.execute_command("""SELECT employees.name, employees.salary, branches.location, SUM(activities.quantity*(-1)*products.price)
                                          FROM employees
                                            LEFT JOIN activities ON activities.activator_id=employees.id
                                            LEFT JOIN branches ON employees.branche=branches.id
                                            LEFT JOIN products ON activities.product_id=products.id
                                          GROUP BY employees.id
                                          ORDER BY employees.name ASC"""):
        total_sales_income = record[3] if record[3] else 0
        print(f"{record[0].decode()} {record[1]} {record[2].decode()} {total_sales_income}")


def detailed_activities_report():
    print('\nActivities report')
    for record in repo.execute_command("""SELECT activities.date, products.description, activities.quantity, employees.name, suppliers.name
                                          FROM activities
                                            LEFT JOIN products ON activities.product_id=products.id
                                            LEFT JOIN employees ON activities.activator_id=employees.id
                                          LEFT JOIN suppliers ON activities.activator_id=suppliers.id
                                          ORDER BY date ASC"""):
        employee_name = f"'{record[3].decode()}'" if record[3] else 'None'
        supplier_name = f"'{record[4].decode()}'" if record[4] else 'None'
        print(f"('{record[0].decode()}', '{record[1].decode()}', {record[2]}, {employee_name}, {supplier_name})")


if __name__ == '__main__':
    main()
