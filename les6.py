class Car:
    _cars = []
    __this_private = 'HELLO'

    def __init__(self, brand, color, vin):
        self.brand = brand
        self.color = color
        self.vin = vin
        self.__light = False
        self._cars.append(self)

    def start_engine(self):
        print('WRUM WRUM')

    def on_off_light(self):
        self.__light = not self.__light

    def get_private(self):
        return self.__this_private

    def islight(self):
        return self.__light


class Robot:

    def __init__(self, name, rtype):
        self.name = name
        self.rtype = rtype

    def say(self):
        print(f'Im {self.name}')


class ElCar(Car):

    def __init__(self, brand, color, engine):
        self.engine = engine
        super().__init__(brand, color, 'fjhfkjfhkfh')

    def bip(self):
        print('BIP BIP')

    def start_engine(self, key=True):
        if key:
            print('SSSSSSSSSS SSSSSSS')
        else:
            super().start_engine()


class Transformer(Car, Robot):

    def __init__(self, name):
        super().__init__('UFO', 'MULTY', '-')
        Robot.__init__(self, name, 'Transformer')
        self.__is_traform = True

    def start_engine(self):
        if self.__is_traform:
            self.say()
        else:
            super().start_engine()

    def transformation(self):
        print('TRANFFORM')
        self.__is_traform = not self.__is_traform


elcar = ElCar('TESLA', 'RED', '234kw')

optimus = Transformer('OPTIMUS PRIME')
print(1)
