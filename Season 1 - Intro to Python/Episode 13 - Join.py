# 13. Join
# it allows to print list a bit better

friends = ['Pythobit','boy','Pythoman']
print(f'My friends are {friends}.')     # Output - My friends are ['Pythobit', 'boy', 'Pythoman'].
# So, the Output needs to be a bit clearer.

friends = ['Pythobit','boy','Pythoman']
friend = ', '.join(friends)
print(f'My friends are {friend}')       # Output - My friends are Pythobit, boy, Pythoman
# Here (, ) comma n space is used as separator, but you can use anything.
