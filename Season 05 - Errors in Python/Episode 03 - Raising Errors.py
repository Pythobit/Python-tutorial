# Raising errors in python

"""
Consider a class garage, to add new car in the garage, we'll write as,

class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def add_car(self, car):
        print('this method is a work in progress..!')

ford = Garage()
ford.add_car('Fiesta')
print(len(ford))

# OUTPUT - this method is a work in progress..!
           0
"""
# Instead of this, we can raise an NotImplementedError as,

class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def add_car(self, car):
        raise NotImplementedError("We can't add car to the garage yet..!")
# Doing this, will give an error that this method is not implemented yet.

ford = Garage()
ford.add_car('Fiesta')
print(len(ford))
"""
Function add_car, now should only accept the parameter being a car object, so how to do that, there is an built-in function
in python called isinstance 
so, we'll raise an TypeError here & remove the NotImplementedError and add self.cars.append(car)
"""
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __repr__(self):
        return f'<Car {self.make} {self.model}>'

class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def add_car(self, car):
        if not isinstance(car, Car):
            raise TypeError(f'Tried to add a `{car.__class__.__name__}` to the Garage, but you can add only `Car` Objects.')
        self.cars.append(Car)
# Note here, we don't need here to use of else because here are we using `if not` keyword, so we don't require an else

ford = Garage()
car = Car('Ford', 'Fiesta')
ford.add_car(car)
print(len(ford))        # OUTPUT - 1
"""
So, what we gonna do is to create a new object
car = Car('Ford', 'Fiesta')
ford.add_car(Car)
now, you can print(len(ford))
"""
"""
When you want an error, raise it's object name of it & put a nice message in it.
* errors are most useful for developers, who are writing code, or someone helping to write code, or working in team."""
