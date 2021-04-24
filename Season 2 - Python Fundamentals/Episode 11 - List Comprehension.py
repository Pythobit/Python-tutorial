# List Comprehension

# Suppose we have list of numbers as given below :
numbers = [0,1,2,3,4]
# and we want to double all the number in the list, i.e: each number to be multiplied by
doubled_numbers = []

for number in numbers:
    doubled_numbers.append(number * 2)
print(doubled_numbers)      # OUTPUT - [0, 2, 4, 6, 8]

# Above method is long and time consuming to run,
# so, we'll use list comprehension instead
doubled_numbers = [number * 2 for number in numbers]
print(doubled_numbers)      # OUTPUT - [0, 2, 4, 6, 8]
# Above method is way easier than that 5 line code above.

""" Also we can use range, instead of using a list.. """
doubled_numbers = [number * 2 for number in range(10)]
print(doubled_numbers)      # OUTPUT - [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Examples
# 01.
friend_ages = [22,31,35,37]
ages = [f'My friend is {age} years old' for age in friend_ages]
print(friend_ages)          # OUTPUT - [22, 31, 35, 37]

# 02.
names = ['Rolf', 'Bob' ,'Jen']
lower = [name.lower() for name in names]
print(lower)                # OUTPUT - ['rolf', 'bob', 'jen']
# Above method will give print the letters in lowercase

# Above method comes best use in user_input..tasks..
#friend = input('Enter your name : ')
friends = ['Rolf','Anne','Jen','Bob','Charlie']
# friends_lower = [name.lower() for name in friends]
#if friend in friends:
#    print(f'{friend} is one of your friend.')       # OUTPUT - Enter your name : Rolf
#                                                               Rolf is one of your friend.
# for the best use
friend = input('Enter your name : ')
friends = ['Rolf','Anne','Jen','Bob','Charlie']
friends_lower = [name.lower() for name in friends]

#if friend.lower() in friends_lower:
#    print(f'{friend} is one of your friend.')       # OUTPUT - Enter your name : jen
#                                                              jen is one of your friend.
# we can also do title casing, meaning that the first letter will be capital and rest letters as lowercase.
print(f'{friend.title()} is one of your friend.')   # OUTPUT - Enter your name : jen
#                                                              Jen is one of your friend.
