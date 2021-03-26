class Book:
    def __init__(self, name, author, year, pages):
        self.__name = name
        self.__author = author
        self.__year = year
        self.__pages = pages

    def info(self):
        return f"Name: {self.__name}, Author: {self.__author}, Year: {self.__year}, Pages: {self.__pages}"


if __name__ == '__main__':
    book1 = Book("Boca", "Tony", 1994, 634)
    print(book1.info())
