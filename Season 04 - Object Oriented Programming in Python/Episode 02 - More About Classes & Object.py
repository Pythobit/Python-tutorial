# More about classes and objects...
# Taking the previous example,
class Student:
    def __init__(self, new_name, new_grades):
        self.name = new_name
        self.grades = new_grades

    def average(self):
        return sum(self.grades) / len(self.grades)

student_one = Student('Rolf Smith', [70, 88, 90, 99])

print(student_one.average())        # OUTPUT - 86.75
# So, what happens when we run the above statement
# python runs print(Student.average(student_one)) in the background to get the OUTPUT -  86.75
# and student_one is being passed as self.
""" Class allows the functionality to store some functions/methods that act on that data as well. """

# SOME BUILT IN FUNCTIONS, YOU'VE ALREADY SEEN.,
int, str, sum(), print(), range
""" * len(my_list) gives you the length of my_list, it also works with Tuples & Strings. """
""" * max(my_list) gives you the maximum number in the my_list (there also min(my_list)). """
""" * round(my_decimal) rounds my_decimal, acc. to the maths rule,(e.g: 3.5 rounds to 4, and if 3.49 rounds to 3)."""
