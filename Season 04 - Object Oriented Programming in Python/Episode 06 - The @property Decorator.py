# The @property Decorator
"""
We've learned previously the functions that are methods inside the class are the pieces of code that do something and
perform an action.
And, here we see weekly_salary method doesn't perform any action, it just calculates and return a value that is based
on Self's Property.
"""

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)


class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary

    def weekly_salary(self):
        return self.salary * 37.5

rolf = WorkingStudent("Rolf", "MIT", 15.50)

rolf.marks.append(57)
rolf.marks.append(99)

print(rolf.weekly_salary())   # O/P - <bound method WorkingStudent.weekly_salary of <__main__.WorkingStudent object at 0x000002023B146670>>
"""
What Output here is telling is that this is the definition of def weekly_salary(self).
Hence, if you want to use the above definition, 
we have to use a decorator called as @property., this turns the method that can be used like so.,
"""

@property
def weekly_salary(self):
    return self.salary * 37.5

print(rolf.weekly_salary)   # O/P - 581.25
"""
So, Here we don't have to put brackets in here.,
We're gonna learn decorator later, & how decorator works is bit complex.
** Use @property decorator only when calculating from object property themselves.
"""
