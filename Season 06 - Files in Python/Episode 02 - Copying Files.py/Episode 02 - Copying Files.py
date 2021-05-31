# Copying files

# Ask user for a list of 3 friends.
# for each friend, we'll tell user whether they're nearby.
# for each nearby friend, we'll save their name to `nearby_friends.txt`.
friends = input('Enter three friends name(separated by commas): ').split(',')

people = open('people.txt', 'r')
people_nearby = [line.strip() for line in people.readlines()]
people.close()

# Making set of friends and peoples
friends_set = set(friends)
people_nearby_set = set(people_nearby)

friends_nearby_set = friends_set.intersection(people_nearby_set)

nearby_friends_file = open('nearby_friends.txt', 'w')

for friend in friends_nearby_set:
    print(f'{friend} is nearby.! Meet up with them.')
    nearby_friends_file.write(f'{friend}\n')

nearby_friends_file.close()
