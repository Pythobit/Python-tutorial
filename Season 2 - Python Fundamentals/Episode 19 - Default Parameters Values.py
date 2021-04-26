# Default Parameter Values

def add(x, y):
    total = x + y
    return total
# Here return will return the total value after calling the function to the function..,
print(add(5,10))        # OUTPUT - 15

# To set a default value, you need to define it in the definition of function..,
def add(x, y=3):    # Here y=3 is the default value given to the function definiton
    total = x + y
    return total
print(add(5))           # OUTPUT - 8

# but you can still write as,
print(add(5,2))         # OUTPUT - 7
# you can also do .,
print(add(x=5))         # OUTPUT - 8

# But if write above code as .,
print(add(x=5, 6))      # OUTPUT - ERROR..!!!
""" This will give an error., i.e: because the starting value has name whereas the preceding variable has no name.. """

# but, here a bit different,
print(add(5, y=3))      # OUTPUT - 8
""" this will work as we've defined a default value, here if you don't have a name in first variable of add function,
but you can have name in the preceding one.., it will run. """

# but, if you do
print(add(y=2))         # OUTPUT - ERROR -- as you'r missing one positional argument - (x)

# Special functions
print(1, 2, 3, 4, 5, sep='-')   # OUTPUT - 1-2-3-4-5

# A Method that is highly discouraged,
default_y = 3

def add(x, y = default_y):
    total = x + y
    print(total)
add(2)                  # OUTPUT - 5

""" now, if you change the value of the default_y, it doesn't changes because when python defines a function, 
it also store the default value of the parameter """
# Even if you change the default value afterwards, it just can't
default_y = 5
add(3)                  # OUTPUT - 5 // As explained above..
