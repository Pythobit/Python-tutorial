# Dealing with errors in Python

# Normal Usage of two classes.
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __repr__(self):
        return f'< Car {self.make} {self.model} >'

class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def add_car(self, car):
        self.cars.append(car)

ford = Garage()
fiesta = Car('Ford', 'Fiesta')
ford.add_car(fiesta)
"""
Normally, we want to make sure that we're adding only cars and nothing else, so what we should do is,
   
    if isinstance(fiesta, Car):
        ford.add_car(fiesta)
    else:
        print('Your car was not a car..!')
    
    from <line 24> onwards
    
instead we can do this at the method add_car
"""
def add_car(self, car):
    if not isinstance(car, Car):
        raise TypeError('Error..!')
    else:
        self.cars.append(car)
"""
An exception might happen if you try ford.add_car(fiesta)
"""
def add_car(self, car):
    try:
        ford.add_car(fiesta)
    except TypeError:
        print('You`r car was not a car.!')
    finally:
        print('this will run always..')

# We can catch multiple errors by adding another except block just below the previous one.
