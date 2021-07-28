# shared state in thread

import time
import random

from threading import Thread

counter = 0

"""
adding time.sleep(random.random()) after each statement is called 'Fizzing',
using this, we'll get an erraneous values
"""


def increment_counter():
    global counter
    time.sleep(random.random())
    counter += 1
    time.sleep(random.random())
    print(f'New Counter Value:{counter}')
    time.sleep(random.random())
    print('-------------')


for x in range(10):
    t = Thread(target=increment_counter)
    time.sleep(random.random())
    t.start()
