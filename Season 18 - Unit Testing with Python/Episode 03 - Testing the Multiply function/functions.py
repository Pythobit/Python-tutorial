from typing import Union


def divide(dividend: Union[int, float], divisor: Union[int, float]):
    if divisor == 0:
        raise ValueError('The Divisor cannot be Zero..!')

    return dividend/divisor


def multiply(*args: Union[int, float]):     # this can take any number of arguments.
    if len(args) == 0:
        raise ValueError('At Least one value must be passed..!')

    total = 1
    for arg in args:
        total *= arg

    return total
