import sqlite3

"""
Concerned with storing and returning books from a CSV file.

format of CSV File :
name, author, read
"""
books_file = 'books.txt'


def create_book_table():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)')

    connection.commit()
    connection.close()


def add_book(name, author):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('INSERT INTO books VALUES(?, ?, 0)', (name, author))

    connection.commit()
    connection.close()


def get_all_books():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM books')
    books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]

    connection.close()
    return books


def mark_book_as_read(name):
    books = get_all_books()
    for book in books:
        if book['name'] == name:
            book['read'] = '1'
    _save_all_books(books)


def _save_all_books(books):
    with open(books_file, 'w') as file:
        for book in books:
            file.write(f'{book["name"]}, {book["author"]}, {book["read"]}\n')
"""
_ before function is used to tell other programmers to not use this function outside the file, and should only be used inside the file and
are known as PRIVATE FUNCTION.
"""


def delete_book(name):
    books = get_all_books()
    books = [book for book in books if book['name'] != name]

    _save_all_books(books)
