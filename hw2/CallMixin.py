class CallMixin:
    def call(self):
        print(f"Calling to {self.fname} {self.lname}, Number: {self.phone}")


class Person(CallMixin):
    def __init__(self, fname, lname, phone):
        self.fname = fname
        self.lname = lname
        self.phone = phone

    def info(self):
        return f"First name: {self.fname}, Last name: {self.lname}, Phone number: {self.phone}"


if __name__ == '__main__':
    p = Person("Givi", "Todua", "599090909")
    p.call()