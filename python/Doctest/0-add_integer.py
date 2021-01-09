#!/usr/bin/python3
"""suma dos enteros"""


def add_integer(a, b):
    """add_integer recibe dos enteros y los suma

    Args:
        a (int, float): argumento que se sumara con b
        b (int, float):  argumento que se sumara con b.

    >>> add_integer(5, 10)
    15

    >>> add_integer(5, 10)
    0

    >>> add_integer(-5, 10)
    5
    """
    return a + b

if __name__ == "__main__":
    import doctest
    doctest.testmod()

