import csv


def read_employees():
    employees = {}

    with open('employee_data.csv') as employee_data_csv:
        employee_data_reader = csv.reader(employee_data_csv)
        employee_data_reader.__next__()

        for employee in employee_data_reader:
            name = employee[0]
            if employees.get(name) is None:
                employees[name] = []

            base_salary = int(employee[1])
            bonus = int(employee[2])
            employees[name].append(base_salary)
            employees[name].append(bonus)

    return employees


def calculate_sum(employees):
    employees_totals = {}
    for employee_name, employee_salaries in employees.items():
        employees_totals[employee_name] = sum(employee_salaries)
    return employees_totals


print(calculate_sum(read_employees()))
