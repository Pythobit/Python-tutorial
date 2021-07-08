# generator class and iterators

class FirstHundredNumbers:
    def __init__(self):
        self.numbers = 0

    def __next__(self):
        if self.numbers < 100:
            current = self.numbers
            self.numbers += 1
            return current
        else:
            raise StopIteration()


my_gen = FirstHundredNumbers()
print(next(my_gen))
print(next(my_gen))

"""
def __next__ is an iterator and class FirstHundredNumbers are not iterable
and there's a difference between iterators and iterable.
"""

