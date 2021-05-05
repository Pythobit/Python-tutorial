# More @classmethod and @staticmethod Examples

class FixedFloat:
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return f'< Fixed-Float {self.amount:.2f} >'

# Here .2f means that python will allow us to print the amount upto 2 decimal places. for e.g.,
print(15.50)    # normally will return 15.5, but if we use .2f python will return 15.50.,

# creating class object.,
number = FixedFloat(18.5746)
print(number)       # OUTPUT - < Fixed-Float 18.57 >


class FixedFloat:
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return f'< Fixed-Float {self.amount:.2f} >'

    def from_sum(self, value1, value2):
        return FixedFloat(value1 + value2)
"""
This will return a float value from the sum of value 1 + value 2
"""
number = FixedFloat(18.5746)
print(number)

new_number = number.from_sum(19.575, 0.787)
print(new_number)           # OUTPUT - < Fixed-Float 20.36 >
"""
# Here, number.from_sum is an instance method, it doesn't have any decorator.

# In Order to use .from_sum object, we need to define FixedFloat object, that we've never used.
Instead of doing this we can make from_sum method @staticmethod
"""
class FixedFloat:
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return f'< Fixed-Float {self.amount:.2f} >'

    @staticmethod
    def from_sum(value1, value2):
        return FixedFloat(value1 + value2)
# Now, you won't be requiring any object, you can call it with class
new_number = FixedFloat.from_sum(19.575, 0.789)
print(new_number)          # OUTPUT - < Fixed-Float 20.36 >

# Now, we'll extend our class..,
class Euro(FixedFloat):
    def __init__(self, amount):
        super().__init__(amount)
        self.symbol = '€'
# Now, we'll override the FixedFloat class using repr dunder function, in order to return Euro class.
    def __repr__(self):
        return f'< Euro {self.symbol} {self.amount:.2f} >'

money = Euro(18.786)
print(money)                # OUTPUT - < Euro € 18.79 >
# What if we do.,
money = Euro.from_sum(16.758, 9.999)
print(money)                # OUTPUT - < Fixed-Float 26.76 >
"""
This will return a Fixed-Float Object, which doesn't make any sense.
We don't want that, instead that we are returning an object of the type of the class we called it with.

We can resolve this bug by changing staticmethod to classmethod in parent class at repr method.
"""
@classmethod
def __repr__(cls, value1, value2):
    return cls(value1 + value2)
# This will gonna return the name of class, e.g: if euro class called, o/p be - < Euro € {value1 + value2} >
"""
You can use classmethod whereever you want, that doesn't need self in it.
* just, if you want to call FixedFloat or Euro class, just use cls, it will automatically interpret what inherited class
object is been calling and will give the desired result.
* So, classmethod makes the method more generic and a bit nicer.
** staticmethod is a simple classmethod with less functionality, also it doesn't allows to inherit.,
"""
# You'll learn about these methods further clearly, as we'll gonna use these method a lot, as we move forward in our Course.
