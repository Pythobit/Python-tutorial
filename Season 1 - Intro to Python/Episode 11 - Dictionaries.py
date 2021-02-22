# 11. Dictionaries

# Dictionary is for when you look for definition of a key to search
# A Dictionary allows you to store keys & Values, is useful when you know the key & get the value back (definition)
friend_ages = {'Pythobit':20,'boy':21,'Pythoman':22}
# so, if you want to know the Pythobit's age, then you must know the key, which is string (Pythobit),then you will get back the value (20)
print(friend_ages['Pythobit'])      # Output - 20

# now, to add values,
friend_ages['Harleen'] = 23  # we're accessing key here & setting a value in it.
print(friend_ages)      # Output - {'Pythobit': 20, 'boy': 21, 'Pythoman': 22, 'Harleen': 23}

# You cannot access key, and value at the same time, this will be given out as invalid
#friend_ages['Pure':24]
#friend_ages['Pure']:24
# Hence, you cannot use colon to add elements in the dictionary, as colon is only used inside the dictionary.

# changing the existing value
friend_ages['Pythobit'] = 21
print(friend_ages)      # Output - {'Pythobit': 21, 'boy': 21, 'Pythoman': 22, 'Harleen': 23}
# you cannot have duplicate keys in dictionary but order of elements is always remains same.
# to store multiple data values,
friends = (
    {'name':'Pythobit','age':21},
    {'name':'boy','age':21},
    {'name':'Pythoman','age':21}
)
# A tuple with lists in it.
print(friends[0]['name'])   # Output - Pythobit
# here, friends[0] -- represents first element of the dictionary

# But we cannot write as,
friends = (
    {'boy':21}
)
# because this will change the meaning, so you need to know the name, by this you cannot access everyone's names before you must know each other name.

# Another Function
# DICT Function
# DICT Function is used to turn data into dictionaries.

# e.g: List of Tuples
friends = [('Pythobit',21),('boy',21),('Pythoman',22)]
friend_ages = dict(friends)
print(friend_ages)     # Output - {'Pythobit': 21, 'boy': 21, 'Pythoman': 22}
