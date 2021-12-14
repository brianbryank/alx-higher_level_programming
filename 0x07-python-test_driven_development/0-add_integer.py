#!/usr/bin/python3
def add_integer(a, b=98):
    """My addition function
    Args:
        a: first integer
        b: second integer
    Returns:
        The return value. a + b
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError('a must be an integer')
    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError('b must be an integer')
    a = int(a)
    b = int(b)
    return (a + b)
