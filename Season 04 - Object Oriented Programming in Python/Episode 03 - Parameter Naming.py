# Parameter Naming...
class Movie:
    def __init__(self, name, year):
        self.name = name
        self.year = year
""" Here, name in self.name is not a variable, it's a property of self, and is gonna created inside self, so don't get confused.
between self.name = name """
""" it defines that property inside self is name accessed by dot(.) and is assigned to a new variable name, that is already defined
 in the scope (i.e: __init__(self, name <--"this one")) """
print(Movie('The Matrix', 1994).name)       # OUTPUT - The Matrix
# but we can do above method using object as,
Matrix = Movie('The Matrix', 1994)
print(Matrix.name)                          # OUTPUT - The Matrix
# You can put object in tuples, lists, dictionaries, anywhere you want..
"""  
*   You cannot ADD one object to another.
*   You cannot MULTIPLY one object to another.
"""
