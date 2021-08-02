import functools    #


user = {
    'username': 'pythobit',
    'access_level': 'user'
}


def user_has_permission(func):
    @functools.wraps(func)      #
    def secure_func(*args, **kwargs):       # updated
        if user.get('access_level') == 'user':
            return func(*args, **kwargs)    # updated
        raise PermissionError
    return secure_func


@user_has_permission
def my_function(panel):
    return f'password for {panel} panel is 1244'

@user_has_permission
def another():
    pass


print(my_function('movies'))
print(another())
