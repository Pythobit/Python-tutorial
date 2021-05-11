# Built-in errors.

"""
I'm gonna tell you the types of errors mostly occurs in the python, so when they appear you know, what they mean,
why they occur, and why they appear, so i'll discussing about these errors, so you won't have to waste your googling
everything.

 1. IndexError
 2. KeyError
 3. NameError
 Errors (1-3) happens when you access something that doesn't have to access in the wrong way.

 4. AttributeError
 This error is fairly related to above errors.

 5. NotImplementedError
 This error can be used very handy.

 6. RuntimeError or GenericError
 7. SyntaxError
 Errors (6-7) occurs when you mess with syntax in python.

 8. IndentationError
 9. TabError
 Errors (8-9) occurs when you mess with spaces and tabs, spaces and tabs varies differently in the editors,

 10. TypeError
 11. ValueError
 errors (10-11) occurs when you the wrong values or values of wrong type to some built-in functions.

 12. ImportError
 13. DeprecationError
"""
"""
1. IndexError :-
        >>> friends = ['Rolf', 'Anne']
        >>> friends[2]
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
        IndexError: list index out of range
        
    Basically, we've defined two friends Rolf, Anne, and we're accessing the 2nd element in the list that doesn't exist in the list,
    as the list has only two elements (i.e: 0 as Rolf, 1 as Anne), when you'll try to access the 2nd element, python will the IndexError,
    as the range will go only upto 1 (Starting from 0)
    
    # NOTICE HERE : Traceback here gives the name of the file, line in the file, function that caused the error, also the description
    or reason of causing the error.
    
2. KeyError :-
        def show_movie_details(movie):
            print(f'Name: {movie["name"]}')
            print(f'Director: {movie["director"]}')
            print(f'Release Year: {movie["release"]}') -- It Should be a 'year'
        
    so, as you can see that in <line 4> instead of this {movie["release"]}, it should be {movie["year"]}, so will get a KeyError,
    
    But, remember that here movie being a dictionary, and accessed the incorrect key, if movie was a list, we'll get a different error.
    
3. NameError :-
        >>> print(hello)
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
        NameError: name 'hello' is not defined
"""

Ep. 02 - Built-in Errors
