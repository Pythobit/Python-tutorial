# Intro to Object oriented programming in python

# Taking an example
my_student = {
    'name': "Rolf Smith",
    'grades': [70, 88, 90, 99]
}
def average_grade(student):
    return sum(student['grades']) / len(student['grades'])

print(average_grade(my_student))        # OUTPUT - 86.75

# here we'll use object oriented programming,
""" An object stores data and actions to do with that data. """
# here we'll define a class
class Student:              # class name generally starts with Capital letter
    def __init__(self, new_name, new_grades):  # defining a function __init__, this is known as special function or dunder functions.
        self.name = new_name        # here self is the default parameter, also we take new_name, and new_grades in order to store the name of the student and,
        self.grades = new_grades    # the grades student scored assigned to new variable, so when the object is called the stored can be called.
        
    def average(self):              # average function to be find the average of the grades of the student number.
        return sum(self.grades) / len(self.grades)
    
