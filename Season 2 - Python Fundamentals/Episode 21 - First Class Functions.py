# First Class Functions
""" This means that strings, integers, anything., we can assigns function variable and we can pass them as
argument to other function. """
def greet():
    print('Hello')
greet()
# but what if we print like this without the parentheses.,
greet
# Still this is also valid python syntax.,
# An example of first class can be that, we can assign above greet as,
hello = greet
hello()                 # OUTPUT - Hello
# hello() - this will call the greet function as we've have make the variable hello equal to greet..,
# ** you can also put it inside a list..
# Example -
avg = lambda seq: sum(seq) / len(seq)
total = lambda seq: sum(seq)
top = lambda seq: max(seq)

students = [
    {"name": 'Rolf', "grades": (67, 90, 95, 100)},
    {"name": 'Bob', "grades": (56, 78, 80, 90)},
    {"name": 'Jen', "grades": (98, 90, 95, 99)},
    {"name": 'Anne', "grades": (100, 95, 100, 100)},
]

for student in students:
    name = student['name']
    grades = student['grades']

    print(f'student: {name}')
    operation = input('Enter "average", "total", "top" : ')

    if operation == "average":
        print(avg(grades))
    elif operation == "total":
        print(total(grades))
    elif operation == "top":
        print(max(grades))

# So the best way to short this, is by associating by creating dictionary.,
operations = {
    "average" : avg,
    "total" : total,
    "top" : max
}

# so, instead of if statement, we can do.,
operation_function = operations[operation]
print(operation_function(grades))

""" but, in OUTPUT, if we write something else, this will give an error, whereas if we use an 'if statement' it will
 not give such an error message, instead of this we can print something another message when the user types something 
 another, we'll study this later in the error handling.. """

# if you want to short the above code more., you can do.,
operations = {
    "average": lambda seq: sum(seq) / len(seq),
    "total": lambda seq: sum(seq),
    "top": lambda seq: max(seq)
}

# Instead of total, top, we can do
operations = {
    "average": lambda seq: sum(seq) / len(seq),
    "total": sum,
    "top": max
}
# as we've done above, we can't do this with the 'average' function as their we are passing two variables..

# Moreover, we are heading to our first project, "Movie Collection" using the python basics fundamentals.
# So, See you there..! @Season 3 : First Milestone Project.
