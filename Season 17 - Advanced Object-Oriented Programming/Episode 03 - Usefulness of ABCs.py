from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    def walk(self):
        print('WlaKING..')

    @abstractmethod
    def num_legs(self):
        pass


class Dog(Animal):
    def __init__(self, name):
        self.name = name

    def num_legs(self):
        return 4


class Monkey(Animal):
    def __init__(self, name):
        self.name = name

    def num_legs(self):
        return 2


animals = [Dog('Bob'), Monkey('Rolf')]
for a in animals:
    print(isinstance(a, Animal))
    print(a.num_legs())
