# Iterating over dictionaries

friend_ages = {"Rolf":25,"Jen":35,"Anne":45,"Bob":55,"Charlie":65}
for name in friend_ages:
    print(name)
# Here we are iterating over dictionary keys and not on values.

# To get the values,
for age in friend_ages.values():
    print(age)
# Here we are iterating over dicitionary values and not over keys.

# NOW, the most common way of iterating over dictionary variable is given below,
# here we'll use destructor for variable, name and age are the destructor syntax,
for name, age in friend_ages.items():
    print(f"{name} is {age} years old.")

# .item(), it allows you to get key and value, i.e: it will give you the list of tuples
