import csv


class Employee:
    def __init__(self, name, surname, age, salary):
        self.__name = name
        self.__surname = surname
        self.__age = age
        self.__salary = salary

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_age(self):
        return self.__age

    def get_salary(self):
        return self.__salary

    def info(self):
        return f"Name - {self.__name}, Surname - {self.__surname}, Age - {self.__age}, Salary - {self.__salary}"


if __name__ == '__main__':
    employees = []
    with open('dataset1.csv', newline='') as cs:
        reader = csv.reader(cs)
        data = list(reader)

    for ind, emp in enumerate(data):
        if ind == 0:
            continue
        employees.append(Employee(name=emp[0], surname=emp[1], age=emp[2], salary=emp[3]))

    min_salary_employee = employees[0]
    max_salary_employee = employees[0]
    for emp in employees:
        if emp.get_salary() < min_salary_employee.get_salary():
            min_salary_employee = emp
        if emp.get_salary() > max_salary_employee.get_salary():
            max_salary_employee = emp

    print(f"Min salary employee -> {min_salary_employee.info()}")
    print(f"Max salary employee -> {max_salary_employee.info()}")
