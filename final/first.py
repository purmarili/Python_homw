class Building():
    def __init__(self, address, price, floors_count):
        self.__address = address
        self.__price = price
        self.__floors_count = floors_count

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def get_floors_count(self):
        return self.__floors_count

    def set_floors_count(self, floors_count):
        self.__floors_count = floors_count

    def print_info(self):
        return f'Address: {self.__address}, Price: {self.__price}, Floors Count: {self.__floors_count}'

    def __gt__(self, other):
        return self.__floors_count > other.get_floors_count()

    def __lt__(self, other):
        return self.__floors_count < other.get_floors_count()


if __name__ == '__main__':
    a = Building('kutaisi', '50$', 12)
    b = Building('samtredia', '140$', 5)
    print(a.print_info())
    print(b.print_info())
    print(a > b)
    print(a < b)
