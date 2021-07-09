# Argument Mutability in python

friends_last_seen = {
    'Rolf': 31,
    'Jen': 2,
    'Anne': 11
}

def see_friend(friends, name):
    print(id(friends))
    friends[name] = 0
    
print(id(friends_last_seen))
print(id(friends_last_seen['Rolf']))

see_friend(friends_last_seen, 'Rolf')

print(id(friends_last_seen['Rolf']))
print(id(friends_last_seen))

### 

friends_last_seen = {
    'Rolf': 31,
    'Jen': 2,
    'Anne': 11
}


def see_friend(friends, name):
    print(friends is friends_last_seen)     # Here we'll use `is` keyword to compare two values in IDs
    friends[name] = 0


see_friend(friends_last_seen, 'Rolf')
"""
when we mutate one, it's changing the property of the dictionary `friends_last_seen`, so if we print below code, it 
will print out to be 0.

Mutability can be dangerous if you change the property of the dictionary after <line 11>, as it will change the 
property through the entire program.
"""
print(friends_last_seen['Rolf'])
