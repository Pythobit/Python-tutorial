# High Order Functions

"""
These are functions that accepts other functions as parameters and run them inside of their own body.
"""
def greet():
    print('hello')

def before_and_after(func):
    print('before...')
    func()
    print('after...')

before_and_after(greet)

# A great example

movies = [
    {'name': 'PK', 'director': 'hassan'},
    {'name': 'sanju', 'director': 'meer'},
    {'name': 'raja', 'director': 'hasprit'},
    {'name': 'hindustani', 'director': 'kaur'},
    {'name': 'jai', 'director': 'kans'}
]

find_by = input('Which property are you looking for (name, director)? : ')
looking_for = input(f'What {find_by} are you looking for.? : ')


def find_movie(expected, finder):
    found = []
    for movie in movies:
        if finder(movie) == expected:
            found.append(movie)
    return found


movie = find_movie(looking_for, lambda movie: movie[find_by])
print(movie or 'No movies Found..!')

# We use high order functions extensively in decorators.
