class SomeError(Exception):
    def __init__(self, txt=''):
        self.txt = txt


class Car:
    __vin = 1

    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.vin = self.__vin
        Car.__vin += 1

    @classmethod
    def create_cars(cls, name, color, vin_range):
        return [cls(name, color) for itm in range(vin_range)]

    @staticmethod
    def some(a, b):
        return a + b

    def __str__(self):
        return f'{self.name}:{self.vin}::{self.color}'


class Factory:
    def __init__(self, car_cls, **kwargs):
        self.car_cls = car_cls
        self.cls_kwargs = kwargs

    def __call__(self, count, **kwargs):
        params = {}
        params.update(self.cls_kwargs)
        params.update(kwargs)
        return [self.car_cls(**params) for _ in range(count)]


factory = Factory(Car, name='Ford', color='White')
cars1 = factory(10)
cars2 = factory(10, color='red')
print(1)
