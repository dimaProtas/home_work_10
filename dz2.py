from abc import ABC, abstractmethod


class Clothes:
    def __init__(self, param):
        self.param = param

    @property
    def cloth(self):
        return f'Сумма затраченной ткани: {self.param / 6.5 + 0.5 + 2 * self.param + 0.3 :.2f}'

    @abstractmethod
    def abstract(self):
        return 'Smth vary abstract'


class Coat(Clothes):
    def cloth(self):
        result = self.param / 6.5 + 0.5
        return f'{result :.2f} \t потребуется ткани для костюма!'
        # return result

    def abstract(self):
        return 'Smth vary abstract second'


class Suit(Clothes):
    def cloth(self):
        result = 2 * self.param + 0.3
        return f'{result :.2f} \t потребуется ткани для пальто!'
        # return result

    def abstract(self):
        return 'Smth vary abstract second'

    # @property
    # def __add__(self, other):
    #     return f'{s.cloth() + c.cloth()} сумма необходимой ткани!'

s = Suit(10)
print(s.cloth())
c = Coat(10)
print(c.cloth())
print(s.abstract())
a = Clothes(10)
print(a.cloth)
