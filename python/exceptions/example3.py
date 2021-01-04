#!/usr/bin/python3
def this_fail():
    x = 1/1
    print('x = ', x)

try:
    this_fail()
except ZeroDivisionError as err:
    print("Manejo de errores en tiempo de ejecucion: ", err)
