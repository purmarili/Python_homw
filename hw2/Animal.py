class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def info(self):
        return f"Name: {self.__name}, Age: {self.__age}"


class Dog(Animal):
    def __init__(self, breed, color, name, age):
        super().__init__(name, age)
        self.__breed = breed
        self.__color = color

    def info(self):
        return Animal.info(self) + f" Breed: {self.__breed}, Color: {self.__color}"


if __name__ == '__main__':
    dog1 = Dog("Corgi", "Yellow", "Jack", 2)
    print(Dog.info(dog1))
