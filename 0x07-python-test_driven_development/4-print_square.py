#!/usr/bin/python3
""" matrix dividednd class """


def print_square(size):
    """
        print name and last name
        Args:
            first_name (str): The first name
            last_name (str): The last name
        Raise:
            TypeError: if first or last name is not string
        Return: print My name is <first name> <last name>
        """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        print('#' * size)
