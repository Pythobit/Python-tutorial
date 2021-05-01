# List Slicing
# Index -     0       1       2     3      4
friends = ['Rolf','Charlie','Bob','Anne','Jen']
# if you want friends between 2 and 4
print(friends[2:4])     # OUTPUT - ['Bob', 'Anne']

# if you want all friends except 1
print(friends[1:])      # OUTPUT - ['Charlie', 'Bob', 'Anne', 'Jen']

# Similarly, as above if you want all friends except 4
print(friends[:4])      # OUTPUT - ['Rolf', 'Charlie', 'Bob', 'Anne']

# if you want all friends
print(friends[:])
""" but there's a key difference, this is not the same list as above, this is a new list, but at this point, 
it really does'nt matter. """

# if you want a friend from the ending of the list, below code will give list counting from the end.
print(friends[-3:])     # OUTPUT - ['Bob', 'Anne', 'Jen']
# here empty ---^ after (: colon), depicts right side list.

# Similarly,  as above
print(friends[-3:4])    # OUTPUT - ['Bob', 'Anne']

# if you want a friend from the starting of the list,
print(friends[:-2])     # OUTPUT - ['Rolf', 'Charlie', 'Bob']
# here empty  ^--- after (: colon), depicts left side list.
