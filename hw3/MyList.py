class MyList:
    def __init__(self, lst):
        self.__lst = lst

    def __add__(self, other):
        for i in other.get_list():
            self.__lst.append(i)
        return self.__lst

    def __mul__(self, other):
        l = self.__lst.copy()
        for i in range(other):
            l += self.__lst
        self.__lst = l
        return self.__lst

    def get_list(self):
        return self.__lst

    def __str__(self):
        return f"'{self.__lst}'"


if __name__ == '__main__':
    s = [1, 2, 3]
    b = [4, 5, 6]
    ml1 = MyList(s)
    ml2 = MyList(b)
    ml3 = ml1 + ml2
    print(ml3)
    print(ml1 * 3)
    print(ml2)
