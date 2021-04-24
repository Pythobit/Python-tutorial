# Prime number with for loop
# PRIME NUMBER : Number divisible by 1 or itself.
""" Erastothene's sieve is not a particularly fast algorithm for finding the prime number of a number,
but it is a simpler one, yaa i know, i also wonder what the more complicated ones look like... """

for i in range(2, 10):
    for j in range(2, i):
        if i % j == 0:
            print(f'{i} equals {j} * {i // j}')
            break
    else:
        print(f'{i} is a prime number.')

""" -- OUTPUT -- 
2 is a prime number.
3 is a prime number.
4 equals 2 * 2
5 is a prime number.
6 equals 2 * 3
7 is a prime number.
8 equals 2 * 4
9 equals 3 * 3
"""
