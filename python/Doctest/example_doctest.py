#doctest_simple_with_docs.py

def my_function(a, b):
    """Returns a * b.

    Works whith numbers:

    >>> my_function(2, 3)
    6

    and strings:

    >>> my_function('a', 3)
    'aaa'
    """
    return a * b

class MyClass:
    pass

def unpredictable(obj):
    """Return a new list containing obj.

    >>> unpredictable(MyClass())
    [<example_doctest.MyClass object at 0x10055a2d0>]
    """
    return [obj]