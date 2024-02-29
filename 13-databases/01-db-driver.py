import sqlite3


def create_connection():
    return sqlite3.connect('test.db')


def create_table(conn):
    conn.execute('''CREATE TABLE IF NOT EXISTS COMPANY
        (ID INT PRIMARY KEY NOT NULL,
        NAME TEXT NOT NULL,
        AGE INT NOT NULL,
        ADDRESS CHAR(50),
        SALARY REAL);''')


def insert_values(conn, cursor):
    cursor.execute('INSERT INTO COMPANY VALUES (1, "A Test", 30, "asdf", 1000)')
    cursor.execute('INSERT INTO COMPANY VALUES (2, "B Test", 20, "asdf", 1000)')
    cursor.execute('INSERT INTO COMPANY VALUES (3, "C Test", 35, "asdf", 1000)')
    cursor.execute('INSERT INTO COMPANY VALUES (4, "D Test", 23, "asdf", 1000)')
    cursor.execute('INSERT INTO COMPANY VALUES (5, "E Test", 33, "asdf", 1000)')
    conn.commit()


class Employee:
    def __init__(self, id, name, age, address, salary):
        self.id = id
        self.name = name
        self.age = age
        self.address = address
        self.salary = salary

    def __str__(self):
        return f'''
        Employee:
        - Id: {self.id}
        - Name: {self.name}
        - Age: {self.age}
        - Address: {self.address}
        - Salary: {self.salary}
        '''


conn = create_connection()
cursor = conn.cursor()

name = input("Please input employee name: ")

# Warning!!! SQL Injection
# res = cursor.execute(f'SELECT * FROM COMPANY WHERE Name = {name}')
res = cursor.execute(f'SELECT * FROM COMPANY WHERE Name = ?', name)

employees = list(
    map(lambda emp: Employee(emp[0], emp[1], emp[2], emp[3], emp[4]), res.fetchall())
)

for employee in employees:
    print(employee)

conn.close()
