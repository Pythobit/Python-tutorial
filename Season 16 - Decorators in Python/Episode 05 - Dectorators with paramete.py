import functools    #


user = {
    'username': 'pythobit',
    'access_level': 'user'
}


def third_level(access_level):
    def user_has_permission(func):
        @functools.wraps(func)      #
        def secure_func(panel):
            if user.get(access_level) == 'user':
                return func(panel)
            raise PermissionError
        return secure_func
    return user_has_permission


@third_level('admin')
def my_function(panel):
    return f'password for {panel} panel is 1244'


print(my_function)

user_has_permission = third_level('admin')
my_function = user_has_permission(my_function)
