from pprint import pprint


class Student:
    def __init__(self, name, age, university, gpa):
        self.name = name
        self.age = age
        self.university = university
        self.gpa = gpa

    def __lt__(self, other):
        if self.gpa < other.gpa:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.gpa > other.gpa:
            return True
        else:
            return False

    def __str__(self):
        return f'name : {self.name}, age: {self.age}, uni: {self.university}, gpa: {self.gpa}'


if __name__ == '__main__':
    s = Student('dato', 15, 'BTU', 3.92)
    s1 = Student('jeka', 15, 'BTU', 2.5)
    print(s)
    print(s1)
    print(s < s1)
    print(s > s1)
