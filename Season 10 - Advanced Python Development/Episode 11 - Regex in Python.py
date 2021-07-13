# Regex in Python

import re

# email = "pythobit@github.com"
# expression = "[a-z]+"
#
# matches = re.findall(expression, email)
# print(matches)      # O/P - ['pythobit', 'github', 'com']
#
# name = matches[0]
# domain = f'{matches[1]}.{matches[2]}'
#
# print(name)         # o/p - pythobit
# print(domain)       # o/p - github.com


# a better way to do
email = "pythobit@github.com"
expression = "[a-z\.]+"     # a change of [\.], so there will be two matches only.

matches = re.findall(expression, email)
print(matches)      # O/P - ['pythobit', 'github', 'com']

name = matches[0]
domain = matches[1]

print(name)         # o/p - pythobit
print(domain)       # o/p - github.com


# Doing the regex, without importing or using it's module

email = 'python@github.com'
parts = email.split('@')

name = parts[0]
domain = parts[1]

print(name)
print(domain)

# A more concise example

# import re

price = 'Price: $1240.45'
expression = 'Price: \$([0-9]*\.[0-9]*)'

matches = re.search(expression, price)
print(matches.group(0))     # Entire Match
print(matches.group(1))     # First thing in brackets

price_number = float(matches.group(1))
print(price_number)
