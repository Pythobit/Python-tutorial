import time
from multiprocessing import Process


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


if __name__ == '__main__':
    process = Process(target=complex_calculation)
    process2 = Process(target=ask_user)
    process.start()
    process2.start()

    start = time.time()

    process.join()
    process2.join()

    print(f'Two processes total time: {time.time() - start}')
