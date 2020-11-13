import random


class TermoK:
    def get(self):
        return random.randint(0, 500)


class TermoC:
    def get(self):
        return random.randint(-300, 500)


class TermoF:
    def get(self):
        return random.randint(-100, 800)


class Temperature:
    __KELVIN_CONST_C = 273.15

    __slots__ = ('kelvin',)

    def __init__(self):
        self.kelvin = 0

    @property
    def celsius(self):
        return self.kelvin - self.__KELVIN_CONST_C

    @celsius.setter
    def celsius(self, value):
        self.kelvin = value + self.__KELVIN_CONST_C

    @property
    def fahrenheit(self):
        return self.kelvin * 1.8 - 459.67

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.kelvin = (value + 459.67) / 1.8


if __name__ == '__main__':
    k = TermoK()
    c = TermoC()
    f = TermoF()
    temp = Temperature()
    temp.kelvin = k.get()
    print(temp.kelvin)
    print(temp.celsius)
    print(1)
