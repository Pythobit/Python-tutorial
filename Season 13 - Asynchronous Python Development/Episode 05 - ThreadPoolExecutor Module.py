# Python Concurrent Futures Module : ThreadPoolExecutor
import time
from concurrent.futures import ThreadPoolExecutor

def ask_user():
    start = time.time()
    user_input = input('Enter your name: ')
    greet = f'Hello {user_input}, nice to see you here..!'
    print(greet)
    print(f'ask_user, {time.time() - start}')


def complex_calculation():
    start = time.time()
    print('Started Calculating..!')
    [x**2 for x in range(20000000)]
    print(f'complex_calculation, {time.time() - start}')


start = time.time()
ask_user()
complex_calculation()
print(f'Single thread total time : {time.time() - start}')


start = time.time()


with ThreadPoolExecutor(max_workers=2) as pool:
    pool.submit(complex_calculation)
    pool.submit(ask_user)

print(f'Two thread total time : {time.time() - start}')
