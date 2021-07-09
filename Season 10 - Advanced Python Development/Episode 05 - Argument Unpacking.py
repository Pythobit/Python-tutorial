# Argument Unpacking

accounts = {
    'checking' : 1234.00,
    'saving' : 2000.00
}


def add_balance(amount: float, name: str) -> float:
    accounts[name] += amount
    return accounts[name]

transactions = {
    (129.34, 'checking'),
    (934.34, 'checking'),
    (378.34, 'checking'),
    (1098.34, 'saving'),
    (2348.34, 'saving'),
    (13458.34, 'saving'),
}

for t in transactions:
    # add_balance(t[0], t[1])
    add_balance(*t)     # doing this unpacks iterables into arguments
    # named arguments, benefits : you can put arguments in any order you want like add_balance(name=t[1], amount=t[0])
    add_balance(amount=t[0], name=t[1])

"""
t[0] will call the first element at index 0, and t[1] will call the second element at index 1

Dictionary unpacking is done using (**data)
"""
