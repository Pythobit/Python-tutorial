def add_all(*args):
    return sum(args)


def pretty_print(**kwargs):
    for k, v in kwargs.items():
        print(f'for {k} we have {v}')


pretty_print(username='pythobit', access_level='admin')
print('--------------')
pretty_print(**{'username': 'pybit', 'access_level': 'user'})
