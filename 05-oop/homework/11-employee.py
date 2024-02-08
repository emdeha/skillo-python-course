class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.messages = []

    def send_message(self, message):
        self.messages.append(message)


class Manager(Employee):
    def __init__(self, name, salary, department):
        self.department = department
        super().__init__(name, salary)


class Team:
    def __init__(self, manager, employees):
        self.manager = manager
        self.employees = employees

    def broadcast_message(self, message):
        self.manager.send_message(message)
        for employee in self.employees:
            employee.send_message(message)
