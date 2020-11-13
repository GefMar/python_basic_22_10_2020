class Car:
    def __init__(self, name, vin):
        self.name = name
        self.vin = vin

    def __str__(self):
        return f'{self.name}:{self.vin}'


class GarageIterator:

    def __init__(self, box):
        self.box = box
        self.idx = 0

    def __next__(self):
        try:
            while True:
                if self.box[self.idx].vin[-1] == '5':
                    self.idx += 1
                    continue
                car = self.box[self.idx]
                self.idx += 1
                return car
        except IndexError:
            raise StopIteration


class Garage:
    def __init__(self, name):
        self.name = name
        self.__box = []

    def set_car(self, *cars):
        self.__box.extend(cars)

    def __getitem__(self, item):
        try:
            return self.__box[item]
        except TypeError:
            for car in self.__box:
                if item == car.vin:
                    return car
        raise ValueError('This is not a current vin or index')

    def __iter__(self):
        return GarageIterator(self.__box)


class Vector:
    def __init__(self, *data):
        self.data = data

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(*map(sum, zip(self.data, other.data)))
        return Vector(*map(lambda x: x + other, self.data))


v1 = Vector(1, 2, 3, 4)
v2 = Vector(9, 8, 7, 6)
v3 = v1 + v2

garage = Garage('Crazy Monkey')

car1 = Car('TESLA', 'jdgjgdjdgjhdgj25')
car2 = Car('Ford', 'ruetwuusodhjffr25')
car3 = Car('BMW', 'fjgfkfkhfkhdls35')

garage.set_car(car1, car2, car3)
car_str = str(car1)
for car in garage:
    print(car)
