#!/usr/bin/python3
#raise_exception_msg = __import__('6-raise_exception_msg').raise_exception_msg
def raise_exception_msg(message=""):
    raise NameError(message)

try:
    raise_exception_msg("C is fun")
except NameError as ne:
    print(ne)