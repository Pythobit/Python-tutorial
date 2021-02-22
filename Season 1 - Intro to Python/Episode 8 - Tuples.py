# 8. Tuples

short_tuple = 'Pythobit','boy'
a_bit_clearer = ('Pythobit','boy')  # Best Notation of tuple
# hence, it's not mandatory to put brackets in tuples

tuple_in_a_list = ['Pythobit','boy']  # this will be referred as a list not as a tuple.
# we need to put a bracket inside the lists, so the python will know that we've inserted a tuple in a list.
tuple_in_a_list = [('Pythobit','boy')]
# But if we write as
not_a_tuple = 'Pythobit'  # this will be considered as a string but not as tuple.

# also, taking an example
friends = ('Pythobit','boy','Pythoman')
friends.append('man')   # Output - ATTRIBUTE ERROR ...!!
# this states that we cannot append any values in tuples.

# but, there's a way to add elements in tuples
friends = ('Pythobit','boy','Pythoman')
friends = friends + ('man',)  # Here comma(,) is used to represent it as a tuple and not as a string.
print(friends)     # Output - ('Pythobit', 'boy', 'Pythoman', 'man')

# LISTS can append or remove an element, whereas TUPLES cannot append or remove.
# Use LISTS, if in future Modifications are required.
