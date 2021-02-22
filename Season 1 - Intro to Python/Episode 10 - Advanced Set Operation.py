# 9. Advanced Set Operations

art_friends = {'Pythobit','boy','Pythoman'}
science_friends = {'boy','harleen'}
# to find difference / compare between these data values.
art_but_not_science = art_friends.difference(science_friends)
science_but_not_arts = science_friends.difference(art_friends)
print(art_but_not_science)      # Output - {'Pythoman', 'Pythobit'}
print(science_but_not_arts)     # Output - {'harleen'}

not_in_both = art_friends.symmetric_difference(science_friends)
print(not_in_both)              # Output - {'harleen', 'Pythobit', 'Pythoman'}

# to find common in both the sets
art_and_science = art_friends.intersection(science_friends)
print(art_and_science)          # Output - {'boy'}

# to find union / all friends
all_friends = art_friends.union(science_friends)
print(all_friends)              # Output - {'Pythoman', 'boy', 'harleen', 'Pythobit'}
