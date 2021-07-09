# Mutable default arguments (Bad Idea)

def create_account(name: str, holder: str, account_holders: list = []):
    account_holders.append(holder)

    return {
        'name' : name,
        'main account holders' : holder,
        'List of account holders' : account_holders
    }


account_1 = create_account('checking', 'Rolf')
account_2 = create_account('savings', 'Jen')

print(account_2)
"""
output - {'name': 'savings', 'main account holders': 'Jen', 'List of account holders': ['Rolf', 'Jen']}

this happens when we create a function i.e: <line 3> list = [], everytime we create a function instead of calling it 
python updates this list and does not create a new list.

two ways to solve are:
1. don't make default argument,
def create_account(name: str, holder: str, account_holders: list):
    & 
declare empty list in the object creation time,
account_1 = create_account('checking', 'Rolf', [])
account_2 = create_account('saving', 'Jen', [])

2. we don't declare account_holders as list but as None, account_holders = None
and we don't need to declare any empty list at time of calling function
but doing we cannot append holders into the list, so we do
if not account_holders:
    account_holders = []
    
account_holders.append(holder)

return ...

"""
