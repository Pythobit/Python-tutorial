"""
Concerned with storing and returning books from a list.
"""
books = []


def add_book(name, author):
    books.append({'name': name, 'author': author, 'read': False})


def get_all_books():
    return books


def mark_book_as_read(name):
    for book in books:
        if book['name'] == name:
            book['read'] = True


# def delete_book(name):            # This is considered as a Bad Practice.
#     for book in books:
#         if book['name'] == name:
#             books.remove(book)

def delete_book(name):
    global books
    books = [book for book in books if book['name'] != name]

"""
SCOPE - as in <line 26> : global books
states that books in local scope = (is equal to the) books in the outer scope 
"""
