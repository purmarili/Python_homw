class Rectangle:
    def __init__(self, _width, _length):
        self.width = _width
        self.length = _length

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return (self.width + self.length) * 2

    def print_info(self):
        return f"Width - {self.width}, Length - {self.length}"


if __name__ == '__main__':
    rec = Rectangle(5, 7)
    print(rec.area(), rec.perimeter())
    print(rec.print_info())