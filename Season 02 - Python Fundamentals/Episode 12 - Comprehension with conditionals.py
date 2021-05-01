# List comprehensions with conditonals

# here an example
ages = [22,35,27,21,20]
odds = [age for age in ages]
# Here --^ goes -^, meaning that the every age in the above list goes to the new age list as specified above.
# if you want only odd ages, you can put an 'if statement'.
odds = [age for age in ages if age % 2 == 1]
print(odds)     # OUTPUT - [35, 27, 21]

# Example
# here we have find our common friends from friends and guests list..
friends = ['Rolf','ruth','charlie','Jen']
guests = ['jose','Bob','Rolf','Charlie','michael']

friends_lower = [f.lower() for f in friends]
guests_lower = [g.lower() for g in guests]

"""                  OR                      """
friends_lower = set([f.lower() for f in friends])
guests_lower = set([g.lower() for g in guests])
print(friends_lower.intersection(guests_lower))     # O/P - {'rolf', 'charlie'}

"""But we won't use set here, as it gives results in lowercase and it's hard to retrieve letters in uppercase.
also sets do not follow any order,.."""
# we'll use list comprehensions here..!!

friends_lower = [f.lower() for f in friends]
present_friends = [
    name.title() for name in guests if name.lower() in friends_lower
]
print(present_friends)      # O/P - ['Rolf', 'Charlie']

# ** Do not nest the list comprehension in one another,
