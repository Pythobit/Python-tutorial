# Some interesting python collections

"""
1. Counter
"""
from collections import Counter

device_temperatures = [13.0, 12.3, 14.0, 12.0, 14.0, 14.0, 15.0]

temp_counter = Counter(device_temperatures)
print(temp_counter)

# you can use it in dictionary
print(Counter({'hello': 5, 'hii': 20, 'hey': 2})['hey'])

"""
2. defaultdict
"""
from collections import defaultdict

coworkers = [('Rolf', 'MIT'), ('Jen', 'Oxford'), ('Rolf', 'Cambridge'), ('Bob', 'Amity'), ('Bob', 'Manchester')]

alma_maters = defaultdict(list)

# for coworker, place in coworkers:
#     if coworker not in alma_maters:
#         alma_maters[coworker] = []
#     alma_maters[coworker].append(place)

""" Instead of doing this we can do, """
for coworker, place in coworkers:
    alma_maters[coworker].append(place)

# if you want to raise an error, if there's an empty list
alma_maters.default_factory = None

print(alma_maters['Rolf'])
#print(alma_maters['Pythobit'])
print(alma_maters['Bob'])

"""
3. OrderedDict
"""
from collections import OrderedDict

o = OrderedDict()
o['Rolf'] = 6
o['Jen'] = 62
o['Jose'] = 16
print(o)

o.move_to_end('Rolf')
o.move_to_end('Jose', last=False)
print(o)

o.popitem()
print(o)

"""
4. namedtuple
"""
from collections import namedtuple

account = ('checking', 1985.65)
Account = namedtuple('Account', ['name', 'balance'])
accountNamedTuple = Account(*account)
print(accountNamedTuple._asdict())

"""
5. deque
"""
from collections import deque

friends = deque(('Rolf', 'Jen', 'Ann'))
friends.append('Bob')
friends.appendleft('Michael')
print(friends)

friends.pop()
friends.popleft()
print(friends)

