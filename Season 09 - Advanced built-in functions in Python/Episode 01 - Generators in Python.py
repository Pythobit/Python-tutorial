# Generator in Python

def hundred_numbers():
    i = 0
    while i < 100:
        yield i
        i += 1


g = hundred_numbers()
print(next(g))
print(next(g))
print(list(g))  # list starts from the number 2, hence generator knows where it left


my_range_obj = range(10)
next(my_range_obj)  # This will give an error, as of range pretend like generator
print(my_range_obj.__repr__())  # O/P - range(0, 10)

