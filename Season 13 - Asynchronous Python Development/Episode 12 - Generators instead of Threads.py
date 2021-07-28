def countdown(n):
    while n > 0:
        yield n
        n -= 1


c1 = countdown(10)
c2 = countdown(20)

print(next(c1))
print(next(c2))
print(next(c1))
print(next(c2))

# Asynchronous python is built around the generators.
