# any() and all() functions in python

friends = [
    {
        'name': 'Kendall',
        'location': 'Washington DC'
    },
    {
        'name': 'Kylie',
        'location': 'San Francisco'
    },
    {
        'name': 'Jennifer',
        'location': 'San Francisco'
    },
    {
        'name': 'Anna',
        'location': 'Washington DC'
    }
]

your_location = input('What are you at..? - ')
friends_nearby = [friend for friend in friends if friend['location'] == your_location]

if any(friends_nearby):     # True if there's at least one, or False if empty
    print('you are not alone..!')

print(all([1, 2, 3, 4, 5]))
