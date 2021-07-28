from collections import deque

friends = deque(('Rolf', 'Jen', 'Anne', 'Bob', 'Adam'))


def friends_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print(f'{greeting}, {friend}')


def greet(g):
    g.send(None)
    while True:
        greeting = yield
        g.send(greeting)


greeter = greet(friends_upper())
greeter.send(None)
greeter.send('Hello')
print('Hello, world.! Multitasking..')
greeter.send('Hello dude')
