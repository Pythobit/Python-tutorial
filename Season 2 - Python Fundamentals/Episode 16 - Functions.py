# Functions
""" We Studied functions like zip, print, enumerate, etc.., but here we'll study how to define your own function. """
""" def is a python keyword used for defining functions.
# def greet():
here, greet() is the function, we've defined and (:) colon is to be followed as of syntax.. """

def greet():
    name = input('Enter your name : ')
    print(f'Hello, {name}')
""" Now, if we run the code, python will run from the first line of code, and recognize that we've defined a function
greet() only, and comes out of the body, overall if we run the above chunk of code, it will not run the body of the 
  function, so we need to call the function..., """
greet()
""" -- OUTPUT -- 
Enter your name : Pythobit
Hello, Pythobit
"""
# we can only call the function, after defining the function only, if we call the function before defining the function,
# it will give an Traceback error..
""" Variables created inside function, die at the end of the function.., """
# So, if you
print(name)     # OUTPUT - Traceback error..!
