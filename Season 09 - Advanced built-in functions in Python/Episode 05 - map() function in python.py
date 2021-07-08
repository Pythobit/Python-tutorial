# map() function in python

friends = ['KenDall', 'Kylie', 'Randy', 'Anna', 'Marie']
start_with_r = filter(lambda friend: friend .starts_with_r('R'), friends)

friends_lower = map(lambda x: x.lower(), friends)
print(next(friends_lower))


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def from_dict(cls, data):
        return cls(data['username'], data['password'])

users = [
    {'username': 'kendall', 'password': '123'}
    {'username': 'iamawesome', 'password': 'youaretoo'}
]

# users = [User.from_dict(user) for user in users]
users = map(User.from_dict, users) # map is more readable

