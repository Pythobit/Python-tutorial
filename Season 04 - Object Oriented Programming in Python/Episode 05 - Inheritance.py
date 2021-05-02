# Inheritance in Python

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

class WorkingStudent:
    def __init__(self, name, school, salary):
        self.name = name
        self.school = school
        self.marks = []
        self.salary = salary

rolf = WorkingStudent('Rolf', 'MIT', 15.50)
print(rolf.salary)                  # OUTPUT - 15.5 (Note here - python neglects last digit as it is zero.)
"""
What we gonna do is we'll extend the WorkingStudent class to add some bracket at the end and type in Student.
As.,
class WorkingStudent(Student):
"""
class WorkingStudent(Student):      # Now, class WorkingStudent is child class of class Student (Parent class)
    def __init__(self, salary):
        self.salary = salary
"""
But, this doesn't work, this will give an error as object called.,
--    rolf = WorkingStudent('Rolf', 'MIT', 15.50)
--    print(rolf.salary)
So, as of now, we'll see that in the class, 'Rolf' will be printed out as Salary and not as name.,
Reason behind this is.,
that it cannot find any other parameter for name or school.,
also, Self in <line 27> : __init__(self, salary), here self is an blank object (i.e: used to pass values)
as their is only one parameter <salary> and the object we've declared < rolf = WorkingStudent('Rolf', 'MIT', 15.50) >
'Rolf' as the first parameter, so it will be evaluated as first parameter 'salary'.
"""
# But, we can resolve it by using super(), this is will call the __init__ method of the parent class.

class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary

# What is happening here is you are just jumping into the parent's class dunder __init__ method, and self is still an
# blank object.

    def weekly_salary(self):
        return self.salary * 37.5   # 37.5 is total hours you can work in UK in a Week.
rolf.marks.append(57)
rolf.marks.append(99)
print(rolf.average())                  # OUTPUT - 78

# but if you do as below,
anna = Student('Anna', 'Oxford')        # And, here we're trying to access the Student class.
print(anna.weekly_salary())            # OUTPUT - ERROR...!!!
"""
Because, the weekly_salary method is not defined in the parent class, and we've inherited < class WorkingStudent > from 
< class Student >
""" 
