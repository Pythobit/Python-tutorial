# incomplete app
Menu = '\nEnter "add" to add a movie, "show" to see list of movies, "find" to find a movie or "quit" to quit: '
movies = [
    {'title': "PK", 'director': "Rajkumar Hirani", 'year': 2014},
    {'title': "A Wednesday", 'director': "Neeraj Pandey", 'year': 2008},
    {'title': "Piku", 'director': "Shoojit Sircar", 'year': 2015},
    {'title': "Bajirao Mastani", 'director': "Sanjay Leela Bhansali", 'year': 2015},
    {'title': "Veer-Zaara", 'director': "Yash Chopra", 'year': 2004}
]


def add_movie():
    title = input('Enter the movie title: ')
    director = input('Enter Director\'s name: ')
    year = input('Enter the movie release year: ')

    movies.append({
        'title': title,
        'director': director,
        'year': year
    })
    print('--> 👍 Movie Added Successfully..!')


def show_movie():
    for movie in movies:
        print_movie(movie)


def print_movie(movie):
    print('------------------------------')
    print(f'Title: {movie["title"]}')
    print(f'Director: {movie["director"]}')
    print(f'Year: {movie["year"]}')
    print('------------------------------')

def find_movie():
    search = input('Enter the movie title you\'re looking for : ')

    for movie in movies:
        if movie['title'] == search:
            print_movie(movie)


user_selection = {
    'add': add_movie,
    'show': show_movie,
    'find': find_movie
}

def menu():
    selection = input(Menu)
    while selection != 'quit':
        if selection in user_selection:
            selected_function = user_selection[selection]
            selected_function()
        else:
            print('Unknown Command..!. Please try again...')

        selection = input(Menu)

menu()
