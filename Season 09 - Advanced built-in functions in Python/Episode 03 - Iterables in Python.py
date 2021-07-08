# iterables in python.

"""
iterables are objects that has an __iter__ method, this method is going to tell that you can iterate over this iterable
"""

class Firsthundrednumbers:
    def __init__(self):
        self.numbers = 0

    def __next__(self):
        if self.numbers < 100:
            current = self.numbers
            self.numbers += 1
            return current
        else:
            raise StopIteration()


class FirsthundredIterables:
    def __iter__(self):
        return Firsthundrednumbers()


print(sum(FirsthundredIterables()))

# Iterating over Iterables
for i in FirsthundredIterables():
    print(i)
# both the dunder __len__ and __getitem__ are iterables.
# iterator - is used to get next value
# iterable - is used to go over all the values of the iterator.

my_numbers = [x for x in [1, 2, 3, 4, 5]]
# generator comprehension
my_numbers_gen = (x for x in [1, 2, 3, 4, 5])

print(next(my_numbers_gen))

