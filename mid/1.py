class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        area = "{:.2f}".format((s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5)
        return area

    def perimeter(self):
        return self.a + self.b + self.c

    def print_info(self):
        print(self.a, self.b, self.c)
        print(f'area -> {self.area()}, perimeter-> {self.perimeter()}')


if __name__ == '__main__':
    t = Triangle(2, 3, 4)
    t.print_info()
    t1 = Triangle(12, 7, 13)
    t1.print_info()
