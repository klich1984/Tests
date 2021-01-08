#ellipsis

class MyClass:
    pass


def unpredictable(obj):
    """Returns a new list containing obj.

    >>> unpredictable(MyClass()) #doctest: +ELLIPSIS
    [<example_doctest.MyClass object at 0x...>]
    """
    return [obj]
