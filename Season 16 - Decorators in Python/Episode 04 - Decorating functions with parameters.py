import functools    #


user = {
    'username': 'pythobit',
    'access_level': 'admin'
}


def user_has_permission(func):
    @functools.wraps(func)      #
    def secure_func(panel):
        if user.get('access_level') == 'admin':
            return func(panel)
        raise PermissionError
    return secure_func


@user_has_permission
def my_function(panel):
    return f'password for {panel} panel is 1244'


print(my_function)
print(my_function.__name__)
print(my_function('movies'))

"""
we cannot use @user_has_permission decorator on other functions, because we're passing a variable panel in there, 
the other function will not be able to receive it.
"""
