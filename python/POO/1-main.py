#!/usr/bin/python3
#Square = __import__('1-square').Square
class Square:
    __size = 0

    def __init__(self, new_size=None):
        self.__size = new_size


my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)

try:
    print(my_square.size)
except Exception as e:
    print(e)

try:
    print(my_square.__size)
except Exception as e:
    print(e)