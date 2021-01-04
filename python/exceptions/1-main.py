#!/usr/bin/python3
#safe_print_integer = __import__('1-safe_print_integer').safe_print_integer
def safe_print_integer(value):
    try:
        print("valor es {:d}".format(value))
        return True
    except ValueError:
        print("valor no es un entero")
        return False

value = 89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = -89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = "Holberton"
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))