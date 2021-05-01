# For loop
""" for loop is used to repeat a method defined times of number : or we can say that
you know that how many times you want to repeat it
** but in python 'for loop' is bit different than other programming languages. """
# here an example
friends = ['Rolf','Jen','Anne']
# You can use list, set, tuples as they are iterables, because they can be iterated.
for friend in friends:
    print(friend)   # Keep a note on indentation, as it is necessary to keep for syntax formation.
# Above code will print the name of the friends in the friends list defined above.
# Example
elements = [0,1,2,3,4,5,6,7,8,9]
for index in elements:
    print(index)    # this will print numbers from 0 to 9.

""" Usually, the variable that is not in use, we've give it as a underscore(_) in python.
    for _ in friends:
        print('Hello World.!')
also to signal other python programmers that this is not in use."""
# Instead of using a list, we can also do,
for index in range(10):
    print("hello")      # this will print the 'hello', about ten times, as mentioned in range(10) -- here 10 depicts 10 times.

""" -- !! SOME TRICKS ABOUT FOR LOOP !! --"""
# 01. to print numbers from specified numbers,
for i in range(5,10):
    print(i)            # this will print numbers from 5 to 10, As 5,6,7,8,9,10
# 02. to print numbers from specified with number gap in between them,
for i in range(2,20,3):
    print(i)            # this will print numbers from 2 to 17, As 2,5,8,11,14,17

# Here as Example
# Student is called as List of dicitionary
Students = [
    {'name': "Rolf", 'grade':90},
    {'name': "Bob", 'grade': 78},
    {'name': "Jen", 'grade': 100},
    {'name': "Anne", 'grade': 80},
]

for student in Students:
    name = Students["name"]
    grade = Students["grade"]

    print(f"{name} has a grade of {grade}")
""" -- !! OUTPUT !! -- 
Rolf has a grade of 90
Bob has a grade of 78
Jen has a grade of 100
Anne has a grade of 80
"""
