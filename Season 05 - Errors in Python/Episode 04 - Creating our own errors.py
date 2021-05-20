# Creating our own errors in python.

"""
This is an example of DocString encapsulated in multiline comma's
"""
print(__doc__)  # OUTPUT - This is an example of DocString encapsulated in multiline comma's

"""
So, as we know that we can raise an error by 
raise TypeError()

we also know that how to create and extend the classes

    raise MyCustomError()

this above piece of code is a class and it has to inherit from one of built-in errors.
"""
class MyCustomError(TypeError):
    pass

raise MyCustomError('An Error message.')
"""
but if we need an error code while printing the error message, but we need to define a new constructor in the class
"""
class MyCustomError(TypeError):
    def __init__(self, message, code):
        #super().__init__(message)
        super().__init__(f'Error {code}: {message}')
        self.code = code

raise MyCustomError('An Error message with error code', 500)    # we'll get a message not the error code
"""
we'll create an new error string as super().__init__(f'Error code {code}: {message}')
* if you don't want to raise an TypeError, you can extend the class from Exception, as it's a base class exception.
X Don't extend the class from the BaseException
"""
