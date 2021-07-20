import logging

from app import books

logger = logging.getLogger('scraping.menu')

USER_CHOICE = '''
Enter one to get Started
  - 'b' to look at 5-star Books.
  - 'c' to look at Cheapest Books.
  - 'n' to get the next available book on the catalogue.
  - 'q' to exit the app.
    
  Enter your choice : '''


def print_best_books():
    logger.info('Getting the Best Books...')
    best_books = sorted(books, key=lambda x: (x.rating * -1, x.price))[:10]    # to get the rating in DESC order and upto 10 books using slicing.
    for book in best_books:
        print(book)


def print_cheap_books():
    logger.info('Getting the Cheapest Books...')
    cheapest_books = sorted(books, key=lambda x: x.price)[:10]  # to get the rating in ASC order and upto 10 books using slicing.
    for book in cheapest_books:
        print(book)


book_generator = (x for x in books)


def print_next_books():
    print(next(book_generator))


user_choices = {
    'b' : print_best_books,
    'c' : print_cheap_books,
    'n' : print_next_books
}


def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input in ('b','c','n'):
            user_choices[user_input]()
        else:
            print('Please Choose a Valid Command..!')
        user_input = input(USER_CHOICE)
    logger.debug('Terminating Program..')

menu()
