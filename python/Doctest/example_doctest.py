#ellipsis

class MyClass:
    pass


def unpredictable(obj):
    """Returns a new list containing obj.

    >>> unpredictable(MyClass()) #doctest: +ELLIPSIS
    [<example_doctest.MyClass object at 0x...>]
    """
    return [obj]


# doctest_hashed_values_test.py
import collections

def group_by_length(words):
    """Returns a dictionary grouping words into sets by length.

    >>> grouped = group_by_length(["python", "module", "of",
    ... "the", "week" ])
    >>> grouped == {2:set(["of"]),
    ...             3:set(["the"]),
    ...             4:set(["week"]),
    ...             6:set(["python", "module"]),
    ...             }
    True

    """
    d = collections.defaultdict(set)
    for word in words:
        d[len(word)].add(word)
    return d
