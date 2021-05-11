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

    as earlier told, it happens when we do not define variable, as the error above scripts : name 'hello' is not defined
    of course, print('hello') would still work because it is interpreted as a string. 
    
4. AttributeError :-
    Attribute Error is pretty popular when you start dealing with objects.,
        
        >>> friends = ['Rolf', 'Jose', 'Charlie']
        >>> friends_nearby = ['Rolf', 'Anna']
        >>> friends.intersection(friends_nearby)
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
        AttributeError: 'list' object has no attribute 'intersection'
        
    Intersection is somethings you can do with sets, but these are 2 lists, and here intersection is not applicable,
    so python will give an error.

5. NotImplementedError :-
    This error you won't be seen most often, but it's a error you can use it in your code.,
    and here how to use it.
        
        class User:
            def __init__(self, username, password):
                self.username = username
                self.password = password
            
            def login(self):
                :raise NotImplementedError('This feature is not applied yet...')
         
    And here instead of returning none, you can raise an error like the above mentioned code and put some description in it.
    so, doing this will raise an error, when you call User.login()
    
6. RuntimeError :-
    It is a pretty generic error, it's not correctly clear, when it's gonna happen, this is not an error, you'll see very often.
        it's essentially a base class error and other error inherits from this.
    A Runtime is an Error that happens anytime, when you are running your program.
    
7. SyntaxError :-
    SyntaxError is an error when you mess in your python code.
    
        class User     -- illegal Syntax (missing semicolon (:) )
            def add():
                c = a + b 
    
    the above provided code is an illegal statement, as it missing a semicolon in front of class name
    
8. IndentationError :-
    Remember blocks of function has to be indented.
    
        def add(x, y):
        return x + y
        // this will give an name error
        
        def add(x, y):
            pass
            
        return x + y
        // this will also give an error, as the return statement is out of the class, this will also return NameError.
        
9. TabError :-
    It frequently occurs when changing editors, so spaces and tabs has difference between them,
    so apply carefully, when applying to syntax
    
10. TypeError :-
     It can be pretty common, it happens when you do something like this
        
        >>> 5 + 5
        10
        >>> 'hi' + 'ha'
        'hiha'
        >>> 5 + 'hi'
        Traceback (most recent call back):
          File '<stdin>', line 1, in <module>
        TypeError: unsupported operand type(s) for +: 'int' and 'str'
        
     at last, we're doing something that we should not do,
     we cannot add an integer and a string, as (+) is also a dunder function.

11. ValueError :-
     It is very common, it happens when built-in functions are provided with incorrect value of correct type
     
        >>> int('20.5')
        Traceback (most recent call back):
          File '<stdin>', line 1, in <module>
        ValueError: Invalid literal for int() with base 10 : '20.5'

    Here, we're turning an int in string but string cannot contain decimal places, and if do so you need to convert it into a float.
    Normally, Built-in functions raise ValueError(s).
    but, if you want to raise the error, we'll study it very next lecture...
    
12. ImportError :-
     It's really popular and is big pain in the ass 😄.
     Here's How.,
     
         # app.py                                           # blog.py
         import blog        ---------------------->         from app import menu                    
                        Importing each other circularly
         def menu():        <----------------------         def do_something():                        
            pass                                                pass
            
     This circular import will cause an ImportError,
     
     If you have such error, feel free to raise an issue, i reply within hours.

13. Deprecation Warning :-
     As it says, it's not a warning, not an error, python tricks you the same way.,
     
        from database import Database
        
        class User:
            def __init__(self, username, password):
                self.username = username
                self.password = password
                
            def register(self):
                Database.write(self.username, self.password)
                raise DeprecationWarning('User#register still works, but it is deprecated.')
                
            @classmethod
            def register_user(cls, username, password):
                Database.write(username, password)
                return cls(username, password)
     
     if you raise one, your program will still crash, but it meants to be you tried something which is deprecated.
     
     Deprecation means it's no longer way to do something, now there's a better way whatever you are trying to do.
     
     * Often, you want it be raising any of these exceptions.
     * You should create your own exceptions, with any better name.
"""
