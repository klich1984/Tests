#!/usr/bin/python3
#safe_print_list = __import__('0-safe_print_list').safe_print_list
def safe_print_list(my_list=[], x=0):
    len_list = 0
    for i in my_list:
        len_list += 1
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
        print()
    except IndexError:
        print()
        return len_list

    return x

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))
