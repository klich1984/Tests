#!/usr/bin/python3
#safe_print_list_integers = \
#    __import__('2-safe_print_list_integers').safe_print_list_integers
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    len_print = 0

    while i < x:
        try:
            print("{:d}".format(my_list[i]), end="")
            len_print += 1
        except ValueError:
            pass
        except TypeError:
            pass
        i += 1

    print()
    return len_print

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list_integers(my_list, 2)
print("nb_print: {:d}".format(nb_print))

my_list = [1, 2, 3, "Holberton", 4, 5, [1, 2, 3]]
nb_print = safe_print_list_integers(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))

nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))