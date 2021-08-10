from typing import Union


def divide(dividend: Union[int, float], divisor: Union[int, float]):
    if divisor == 0:
        raise ValueError('The Divisor cannot be Zero..!')

    return dividend/divisor
