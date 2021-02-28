# 9. Sets

# Curly braces are used to represent sets.
# Sets have no order of elements, so it can place elements at either place.
# another reason, Sets are easier to use to compare each other in very basic form.

art_friends = {'Pythobit','boy'}
science_friends = {'Pythoman','man'}
# to add two sets,
art_friends.add('harleen')
print(art_friends)  # Output - {'boy', 'Pythobit', 'harleen'}
# to remove any element,
art_friends.remove('boy')
print(art_friends)  # Output - {'harleen', 'Pythobit'}
