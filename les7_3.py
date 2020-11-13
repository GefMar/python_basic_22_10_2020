from abc import ABC, abstractmethod


class Some(ABC):

    @abstractmethod
    def hello(self):
        pass

    @abstractmethod
    def buy(self):
        pass

    @abstractmethod
    def bye(self) -> str:
        pass

    def hi(self):
        return f'{self.hello()}: {self.buy()}, {self.bye()}'


class WrapMaster:

    def __init__(self):
        self.name = 'dkjhdhdkjd'

    def set_some(self, value: Some):
        pass


class SomeLogic(Some):
    def __init__(self, name):
        self.name = name

    def hello(self):
        return 'hello'

    def buy(self):
        return 1

    def bye(self) -> str:
        return 1


some = SomeLogic('HGDHGSJ')

print(1)
