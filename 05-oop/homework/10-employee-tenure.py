from datetime import datetime
import math


class Employee:
    def __init__(self, name, start_date, phone):
        self.name = name
        self.start_date = start_date
        self.phone = phone

    def tenure(self):
        if not isinstance(self.start_date, datetime):
            return

        delta = datetime.now() - self.start_date
        return math.floor(delta.days / 365)


employee_one = Employee("Tsvetan", datetime(2000, 1, 1), "123")
print("tenure", employee_one.tenure(), "years")
