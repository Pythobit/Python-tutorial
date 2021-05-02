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
    def __init__(self, new_name, new_grades):  # defining a function __init__, this is known as special function or Dunder functions.
        self.name = new_name        # here self is a blank object, also we take new_name, and new_grades in order to store the name of the student and,
        self.grades = new_grades    # the grades student scored assigned to new variable, so when the object is called the stored can be called.

    def average(self):              # average function to be find the average of the grades of the student number.
        return sum(self.grades) / len(self.grades)      # Returning the calculated average value to the average function.

student_one = Student('Rolf Smith', [70, 88, 90, 99])
# here object is that store some data, & we're tell it what data to store.

""" When the object is created, it is created before we call any of these functions, then it immediately calls this '__init__' 
dunder function, the new empty object created gets passed to the self parameter in the dunder init function, so now self is blank,
an empty object that has essentially nothing in it., and as the python is structured.,
from the object created at line 'Rolf Smith' will be passed to new_name as a second parameter., and [70,88,90,99] will be passed to 
new_grades as third parameter. """

"""  very very important here...!
 self is an blank object that was created before calling the dunder init function, when we came to the first line, we know, 
 we have these values, so we use a dot(.) here in order to access the something inside it, and what we gonna access is that 
 is the name thing, because self is an blank object, it doesn't have a variable called name inside it. """

""" what is this doing is that, it is creating a variable name that lives inside this blank object called self, you can change it
if you want name it my object, thats totally fine, but the convention in python calls it self. """

""" now the self.name is the new variable created, and we are giving the variable the value of new_name which is Rolf Smith. """
# we can access some special property of it, as below
print(student_one.name)     # OUTPUT -  Rolf Smith

""" what if we print(student_one.name) # OUTPUT -  Rolf Smith """
print(student_one.__class__)    # OUTPUT - <class '__main__.Student'>
""" what if we print(student_one.__class__) # OUTPUT - <class '__main__.Student'> """
# and as now, object student_one knows it has a Student defined, it has now defined name and grades.
# but if we want another student say student_two,
student_two = Student('Charlie', [78, 89, 86, 100])
print(student_two.name)         # OUTPUT - Charlie
print(student_two.average())       # OUTPUT - 88.25

# NOTHING IS MAGICAL HERE, JUST PASSING OF DATA FROM ONE PLACE TO ANOTHER...
# JUST PRACTICE IN YOUR IDE, you'll get them correctly.

""" now, we've created objects, we know we can define multiple objects and they're all are just independent blank things
 that we've assigned this variables to .."""
