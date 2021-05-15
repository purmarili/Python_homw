class Animal:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def info(self):
        return f"Name: {self.__name}"


class Dog(Animal):
    def __init__(self, name, age, color):
        super().__init__(name)
        self.__age = age
        self.__color = color

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def info(self):
        return Animal.info(self) + f", Age: {self.__age}, Color: {self.__color}"


if __name__ == '__main__':
    dog = Dog('dato', 12, 'shavi')
    dog1 = Dog('jeka', 11, 'shavtuxa')
    print(dog.info())
    print(dog1.info())