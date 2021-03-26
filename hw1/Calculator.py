class Calculator:
    def add(self, first, second):
        return first + second

    def subtract(self, first, second):
        return first - second

    def divide(self, first, second):
        return first / second

    def multiply(self, first, second):
        return first * second


if __name__ == '__main__':
    calc = Calculator()
    print(calc.add(5, 7))
    print(calc.subtract(5, 7))
    print(calc.divide(14, 3))
    print(calc.multiply(14, 3))
