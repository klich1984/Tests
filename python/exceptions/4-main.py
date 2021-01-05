#!/usr/bin/python3
#list_division = __import__('4-list_division').list_division
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    idx = 0

    while idx < list_length:
        try:
            new_list.append(my_list_1[idx]/my_list_2[idx])
        except (ZeroDivisionError, TypeError, IndexError):
            new_list.append(0)
        finally:
            idx += 1
    return new_list

my_l_1 = [10, 8, 4]
my_l_2 = [2, 4, 4]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)

print("--")

my_l_1 = [10, 8, 4, 4]
my_l_2 = [2, 0, "H", 2, 7]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)