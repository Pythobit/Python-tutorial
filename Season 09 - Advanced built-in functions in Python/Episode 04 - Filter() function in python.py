# filter() function in python

friends = ['Kendall', 'Kylie', 'Randy', 'Anna', 'Marie']
start_with_r = filter(lambda friend: friend .starts_with_r('R'), friends)

#                           OR

# we can do above with generator comprehension.
another_starts_with_r = (f for f in friends if f.startswith('R'))

#                           OR

# or with a custom filter function
def custom_filter(func, iterable):
    for i in iterable:
        if func(i):
            yield i
# and by changing the line 4 as start_with_r = custom_filter(func, iterable)
