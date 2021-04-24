# Set and Dictionary Comprehensions

friends = ['Rolf','ruth','charlie','Jen']
guests = ['jose','Bob','Rolf','Charlie','michael']

friends_lower = set([f.lower() for f in friends])
guests_lower = set([g.lower() for g in guests])

# Instead of using the set function, we can use as.
friends_lower = {f.lower() for f in friends}
guests_lower = {g.lower() for g in guests}

# But the problem here occurs is that we can't get names in upper case, it's bit hard to retrieve in uppercase.
# but we want the name to be  uppercase,
present_friends = {name.title() for name in friends_lower.intersection(guests_lower)}
print(present_friends)          # OUTPUT - {'Rolf', 'Charlie'}
# ** Sets removes duplicates if it consists,
# Example
friends = ['Rolf', 'Bob', 'Jen', 'Anne']
time_since_seen = [3, 7, 15, 4]

long_timers = {
    friends[i] : time_since_seen[i]
    for i in range(len(friends))
}
print(long_timers)      # OUTPUT - {'Rolf': 3, 'Bob': 7, 'Jen': 15, 'Anne': 4}

# To see friends more than 5 years,
long_timers = {
    friends[i] : time_since_seen[i]
    for i in range(len(friends))
        if time_since_seen[i] > 5
}
print(long_timers)      # OUTPUT - {'Bob': 7, 'Jen': 15}
# here the friends who have known me for more than 5 years...
