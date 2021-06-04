# from common.file_operations import save_to_file    [X] <-- Wrong Way
# from utils.common.file_operations import save_to_file [+1] <-- Correct
# from .common.file_operations import save_to_file      [+1] <-- Correct
"""
Above methods are : Relative imports : that starts from current file we're working with and it can go down.
--------!!!!!---------!!!!!!!--------!!!!!!!!!!----------
Running find.py will give an error `__main__` module not found.
"""


def find_in(iterable, finder, expected):
    for i in iterable:
        if finder(i) == expected:
            return i
    raise NotFoundError(f'{expected} not found at provided iterables.')


class NotFoundError(Exception):
    pass
