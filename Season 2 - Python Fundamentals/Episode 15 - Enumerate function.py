# Enumerate function
""" We can use this to turn list into something new... """
friends = ['Rolf', 'Bob', 'Anne']
for friend in friends:
    print(friend)

# but we need to get the number with each name of the friend..
counter = 0
for friend in friends:
    print(counter)
    print(friend)
    counter = counter + 1
# but this doesn't work according to our need, so we apply enumerate function here..,

for counter, friend in enumerate(friends):
    print(counter)
    print(friend)
# this also works as same but the ky difference is that we have to code less in the above method..,

# or we can also print as..,
print(list(enumerate(friends)))         # OUTPUT - [(0, 'Rolf'), (1, 'Bob'), (2, 'Anne')]
""" so, enumerate gonna give a number to each tuple.. """

""" you can print in dict """
print(dict(enumerate(friends)))         # OUTPUT - {0: 'Rolf', 1: 'Bob', 2: 'Anne'}

# enumerate function works same as the zip function..
