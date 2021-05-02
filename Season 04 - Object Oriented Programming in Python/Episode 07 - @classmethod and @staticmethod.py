# @classmethod and @staticmethod in Python

# Taking an Example from the previous tut.,
class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)
"""
Till now, We've have learnt dunder __init__ and __len__ function, they'll have something in common
(i.e: self that is an blank object.)
"""
rolf = Student('Rolf', 'MIT')
rolf.marks.append(78)
rolf.marks.append(99)
print(rolf.average())
# here in the above print function, what python is doing in the background is that.,
# print(Student.average(rolf))
"""
Here, as we know that in object < rolf = Student('Rolf', 'MIT') > "Rolf" is getting passed as first parameter name in the init function.,
and the "MIT" as the second parameter as school, and < rolf.marks.append(78), rolf.marks.append(99) > as to append marks in the marks 
empty list as in the <line 8>.
"""
# Coming to the Decorator's - @classmethod and @staticmethod.
class Foo:
    @classmethod
    def hi(cls):
        print(cls.__name__)
"""
* But, you do need an init in every class, you can just ignore it, you won't have to define any property, thats totally fine. 
i renamed the first parameter as 'cls' instead of 'self', that just to tell me that this is a class method.
& this parameter is going to hold the value of the class that is called with.(i.e: Foo)
"""
# Making Object.,
my_object = Foo()
my_object.hi()              # OUTPUT - Foo (i.e: the name of the class)

"""
What's happening in the background is,
my_object is getting passed as the first argument,
now, object's class is getting passed through first argument.
"""
# THESE ARE ONLY SYNTAX, IN NEXT LEC. WE'LL STUDY SOME EXAMPLES RELATED TO THIS.


class Bar:
    @staticmethod           # this staticmethod takes no parameter.
    def hi():
        print('Hello, i don\'t take parameter.')

another_object = Bar()
another_object.hi()         # OUTPUT - Hello, i don't take parameter.
"""
these are pieces of syntax are just, so that what method takes in.

** @classmethod , when someone wants to have access to the class.

** @staticmethod , when you want a method here, that doesn't use the current object or class but it's somehow 
related to the class.
"""
