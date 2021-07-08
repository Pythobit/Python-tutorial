# Mutability in Python

"""
Mutable - a piece of data that you can change after you've created it.
InMutable - a piece of data that you cannot change after you've created it.
"""

# object 1
friends_last_seen = {
    'Rolf': 31,
    'Jen': 2,
    'Anna': 3
}
print(id(friends_last_seen))    # this will display a new id everytime the code runs.

# object 2
friends_last_seen = {
    'Rolf': 31,
    'Jen': 2,
    'Anna': 3
}
print(id(friends_last_seen))

"""
Both the object 1 and 2 are different, as the first object is occupying some space in the RAM at some time,
and the object 2 gives different id when it runs. 
"""
# now changing the object 2 data, this is known as Mutated data

friends_last_seen['Rolf'] = 0
print(id(friends_last_seen))
"""
The above code gives the same id as of the object 2, as because we've mutated it and not created anything, and this 
process of mutating a data is known as Mutability.

there are some things that are InMutable like Integer, Floats, Strings, Tuples
"""
my_int = 5
print(id(my_int))   # this will return an id of the integer, but you cannot change the integer value, because 5 is always 5
# if we do like the below method,
my_int = my_int + 1
print(id(my_int))   # id will be kind of similar but there will be a slight difference.

# Lists however are mutable,

friends = ['Rolf', 'Jen']
print(id(friends))

friends.append('Anna')
print(id(friends))
# the above both will have same id's
"""
However, note here that we haven't created a list but mutated it from the friends list.
"""
