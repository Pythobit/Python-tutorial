# Destructing Syntax
# Using the destructing syntax make easy to read the code, and more understandable.
Currencies = 0.8, 1.2
usd, eur = Currencies
""" Here the first value will be assigned to the usd, and second to eur,
 As, usd = 0.8, eur = 1.2 """

# Example
friends = [("Rolf",35),("Jen",23),("Anne",21),("Bob",36)]
for friend in friends:
    print(friend)
""" -- !! OUTPUT !! -- 
('Rolf', 35)
('Jen', 23)
('Anne', 21)
('Bob', 36)
"""
# Instead of doing the above for loop code
for name, age in friends:
    print(f"{name} is {age} years old.")
""" -- !! OUTPUT !! -- 
Rolf is 35 years old.
Jen is 23 years old.
Anne is 21 years old.
Bob is 36 years old.
"""
# This Syntax makes codes more easy to understand.
