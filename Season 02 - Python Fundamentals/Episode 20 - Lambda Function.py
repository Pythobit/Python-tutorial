# Lambda Functions
""" Lambda Functions are used to get inputs, do a little amount of processing and return the outputs. """
def divide(x, y):
    return x / y
divide = lambda x,y: x / y
print(divide(15,3))             # OUTPUT - 5.0

# but, what if you define straight lambda function.,
lambda x,y: x / y
# Python will define this function & immediately destroys it..
# But, there is a way, you can run this function with enclosed (parentheses).
(lambda x,y: x / y)(15,3)
# doing the above method, so you are telling the python to execute the first parentheses, and then the second.,
""" line: 12, this statements will evaluate, but nothing gets printed out., so, we need to pass it through 
print function, in order to get the result.. """
print((lambda x,y: x / y)(15,3))    # OUTPUT - 5.0

# Example -
def average(sequence):
    return sum(sequence) / len(sequence)

students = [
    {"name": 'Rolf', "grades": (67, 90, 95, 100)},
    {"name": 'Bob', "grades": (56, 78, 80, 90)},
    {"name": 'Jen', "grades": (98, 90, 95, 99)},
    {"name": 'Anne', "grades": (100, 95, 100, 100)},
]
for student in students:
    print(average(student['grades']))
""" -- OUTPUT -- 
88.0
76.0
95.5
95.75
"""
# Instead of writting this chunk of code by defining functions.
average = lambda sequence : sum(sequence) / len(sequence)

""" lambda function are used for getting inputs, returning outputs & not performing what the print function does.. """
