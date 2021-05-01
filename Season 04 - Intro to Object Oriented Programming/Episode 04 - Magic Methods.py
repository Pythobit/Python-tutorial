# Magic Methods
# Here, are some new dunder functions.
class Student:
    def __init__(self, name):
        self.name = name

# But here are some more.,
# Let's take an example..
movies = ['Matrix', 'Finding Nemo']
print(movies.__class__)             # OUTPUT - <class 'list'>
""" list is an object..
Python automatically creates defined list into it's classes.
So, if you print as below.,
"""
print('hii'.__class__)              # OUTPUT - <class 'str'>
# Everything in python is an object.
"""
Q. What does list mean to be a object..? 
--> it means that everything we can do with the list, we can do with their own classes.
"""
# Here's an Example.,
print(len(movies))                  # OUTPUT - 2


class Garage:
    def __init__(self):
        self.cars = []

ford = Garage()
print(ford.cars)                    # OUTPUT - [] (i.e: empty list()

# But if we do append.,
ford.cars.append('Fiesta')
ford.cars.append('Focus')
print(ford.cars)                    # OUTPUT - ['Fiesta', 'Focus']

# But if we print as below.,
print(len(ford))                    # OUTPUT - ERROR..!!

"""
Python doesn't know what garage length meant to be...!
So, in order to tell python what the length of garage should be.,
So, we need to define another dunder function.
"""
def __len__(self):
    return len(self.cars)

print(len(ford))                    # OUTPUT - 2
# But, if we print(ford[0]).., it will an error..!

# So, we'll define another dunder function.,
def __getitem__(self):
    return self.cares[i]

print(ford[0])                      # OUTPUT - Fiesta
"""
You'll be only need __getitem__ and __len__ to be able to for loop over an object.
You can iterate over garage class, as below given
"""
for car in ford:
    print(car)
# but, only if you have above 2 new dunder functions defined..,
# Another new dunder function.,
def __repr__(self):
    return f'<Garage {self.cars}>'

def __str__(self):
    return f'Garage with {len(self)} cars.'
# Now, if you print..,
print(ford)                         # OUTPUT - Garage with 2 cars.
"""
Q. So, what to do to get __repr__ dunder function..!
--> for __repr__ dunder function, we'll study it later in the debugging part..,
* if you want to use from __repr__ or __str__ dunder functions, you can use repr, it's a better approach.
"""
