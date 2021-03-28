class Dog:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def info(self):
        return f"Name: {self.__name}"


class Husky(Dog):
    def __init__(self, name, age):
        super().__init__(name)
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def info(self):
        return f"Name: {Dog.info(self)}, Age: {self.__age}"


if __name__ == '__main__':
    dog = Dog("Jeka")
    print(dog.get_name())
    print(dog.info())
    husky1 = Husky("Chapa", 12)
    husky2 = Husky("Tony", 5)
    husky3 = Husky("Hus", 2)
    print(husky1.info())
    print(husky2.info())
    print(husky3.info())
