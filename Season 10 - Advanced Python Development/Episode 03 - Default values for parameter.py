# default values for parameter

"""
any argument that has default value has to follow argument, that do not have default value.
if not done python will throw an error
SyntaxError : Non default parameter follows default parameter.
example at <line 15> with `name` keyword
"""
accounts = {
    'checking' : 1985.00,
    'savings' : 2000.00
}


def add_balance(amount: float, name: str = 'checking') -> float:
    """ Function to update the balance of the account and return the new balance. """
    accounts[name] += amount
    return accounts[name]

add_balance(500.00)

print(f"Savings Account - {accounts['savings']}")
print(f"Checking Account - {accounts['checking']}")
