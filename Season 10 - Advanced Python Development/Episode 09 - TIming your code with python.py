# Timing your code

import time


def powers(limit):
    return [x**2 for x in range(limit)]

# start = time.time()     # that means time module and the time() function within that module gives current time in seconds since 1970.
# powers(5000000)
# end = time.time()
#
# print(end - start)


def measure_runtime(func):
    start = time.time()
    func()
    end = time.time()
    print(end - start)

measure_runtime(lambda: powers(500000))

import timeit       # timeit is used to get the time that the running function will be going to take.

print(timeit.timeit('[x**2 for x in range(10)]'))
