  # 6. Booleans & Comparisons
# Booleans start with Capital letters i.e: True, False
# also Truthy = True, Falsy = False

age = 20
is_over_age = age >= 18  # This (age >= 18) is a boolean comparison and comes out to be True, if comparison is correct.
is_under_age = age < 18
is_equal = age == 20

# Statement which will compare between our number & users number
my_num = 5                                  # Output
user_num = int(input("Enter a number: "))   # Enter a number: 5     | Enter a number: 4
print(my_num == user_num)                   # True                  | False

# AND & OR
# AND
age = int(input('Enter your age: '))        # Output
learn = age > 0 and age < 150               # Enter your age: 20    | Enter your age: 160
print(f"You can learn: {learn}")            # You can learn: True   | You can learn: False

# Practice some bools
print(bool(35))         # Output - True
print(bool("Rolf"))     # Output - True
print(bool(0))          # Output - False
print(bool(''))         # Output - False

x = True and False
print(x)             # Output - False
# This will check if 1st condition is True & will return second condition i.e: False
x = 34 and 0
print(x)            # Output - 0    # i.e: False
# Same with OR, Using OR gives the first condition, if it is true & vice versa.
x = 34 or 0
print(x)            # Output - 34   # i.e: True

# AND gives you the first value if it is false,Otherwise it gives you the second value.
# OR gives you the first value if it is True, Otherwise it gives you the second value.

name = input('Enter name: ')        # Enter name:   **Pressed ENTER
sname = input('Enter surname: ')    # Enter surname: Boy
greet = name or f"Mr. {sname}"
print(greet)                        # Mr. Boy

# NOT
print(not False)    # Output - True
print(not True)     # Output - False
