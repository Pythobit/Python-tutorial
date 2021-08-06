from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    def walk(self):
        print('WlaKING..')

    @abstractmethod
    def num_legs(self):
        pass


class Dog:
    def __init__(self, name):
        self.name = name

    def num_legs(self):
        return 4


class Monkey:
    def __init__(self, name):
        self.name = name

    def num_legs(self):
        return 2


d = Dog('Rottie')
print(d.num_legs())
