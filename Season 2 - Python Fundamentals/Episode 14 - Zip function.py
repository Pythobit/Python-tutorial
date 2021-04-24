# Zip Function
""" Zip function combines two or more into one... """
friend = {'Rolf','Jen','Bob','Anne'}
time_since_seen = [3, 7, 15, 4]

long_timers = dict(zip(friend, time_since_seen))
print(long_timers)                  # O/P - {'Anne': 3, 'Jen': 7, 'Rolf': 15, 'Bob': 4}

# Also we can make it in list too...
long_timers = list(zip(friend, time_since_seen))
print(long_timers)                  # O/P - [('Rolf', 3), ('Anne', 7), ('Bob', 15), ('Jen', 4)]

long_timers = list(zip(friend, time_since_seen, [1, 2, 3, 4, 5]))
print(long_timers)                  # O/P - [('Bob', 3, 1), ('Jen', 7, 2), ('Anne', 15, 3), ('Rolf', 4, 4)]
# Here zip will ignore the last element ( 5 ) in the list, and ignore matching to time_since_seen list...

# An interesting Fact -
long_timers = zip(friend, time_since_seen)
print(long_timers)                  # O/P - <zip object at 0x0000015FD8496DC0>
# we will study about the above output further...
