user = {
    'username': 'pythobit',
    'access_level': 'admin'
}


def user_has_permission(func):
    def secure_func():
        if user.get('access_level') == 'admin':
            return func()
        raise PermissionError
    return secure_func()


@user_has_permission
def my_function():
    return 'password for admin is 1244'


print(my_function)
print(my_function.__name__)
