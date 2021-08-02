user = {
    'username': 'pythobit',
    'access_level': 'admin'
}


def user_has_permission(func):
    def secure_func():
        if user.get('access_level') == 'admin':
            return func()
    return secure_func()


def function():
    return 'password for admin is 1244'


my_secure_function = user_has_permission(function)
print(my_secure_function())
