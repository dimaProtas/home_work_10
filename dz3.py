class Cell:
    def __init__(self, param):
        self.param = int(param)


    def __add__(self, other):
        return self.param + other.param


    def __sub__(self, other):
        result = self.param - other.param
        if result < 0:
            return f'Разность двух клеток {result} < 0'
        else:
            return result
        return


    def __mul__(self, other):
        return self.param * other.param


    def __truediv__(self, other):
        return self.param // other.param


    def make_order(self, row):
        result = ''
        for i in range(int(self.param / row)):
            result += '*' * row + '\n'
        result += '*' * (self.param % row) + '\n'
        return result

a = Cell(7)
b = Cell(2)
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a.make_order(5))