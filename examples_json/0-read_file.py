#!/usr/bin/python3
# Funcion que lee el texto e imprime en la salida estandar (UTF-8)

import json


def read_file(filename=""):
    """Lee un archivo y lo imprime en la salida

    Args:
        flename (str): Archivoa leer. Defaults to "".
    """
    with open(filename, 'r' ,encoding='utf-8') as fd:
        read_data = fd.read()
        print(read_data)

# Patch absolute
read_file('/home/klich1984/holbeton/Tests/examples_json/my_file_0.txt')