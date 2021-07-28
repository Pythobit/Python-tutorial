# Queueing with shared state in thread

import time
import random
import queue

from threading import Thread

counter = 0
job_queue = queue.Queue()       # Things to be printed out..
counter_queue = queue.Queue()   # Amounts by which to increase the counter


def increment_manager():
    global counter
    while True:
        increment = counter_queue.get()     # This waits until an item is available and then locks the queue.
        old_counter = counter
        counter = old_counter + increment
        job_queue.put((f'New Counter Value is : {counter}', '-------------'))
        counter_queue.task_done()   # This unlocks the queue


Thread(target=increment_manager, daemon=True).start()


def printer_manager():
    while True:
        for line in job_queue.get():
            print(line)
        job_queue.task_done()


Thread(target=printer_manager, daemon=True).start()


def increment_counter():
    counter_queue.put(1)


worker_threads = [Thread(target=increment_counter) for thread in range(10)]

for thread in worker_threads:
    thread.start()

for thread in worker_threads:
    thread.join()


counter_queue.join()
job_queue.join()

"""
You can add fizzing in here, it will work smoothly, and squentially .
"""
