from collections import deque
from types import coroutine

friends = deque(('Rolf', 'Jen', 'Anne', 'Bob', 'Adam'))


@coroutine
def friends_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print(f'{greeting}, {friend}')


async def greet(g):
    print('Starting coroutine...')
    await g
    print('Ending coroutine...')


greeter = greet(friends_upper())
greeter.send(None)
greeter.send('Hello')

greeting = input('Enter the greeting :')
greeter.send(greeting)
greeting = input('Enter the greeting :')
greeter.send(greeting)
greeting = input('Enter the greeting :')
greeter.send(greeting)
