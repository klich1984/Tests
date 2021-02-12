#!/usr/bin/python3
"""  Escribir en un texto """

def write_file(filename="", text=""):
    """Escribe lo ingresado a un texto si no existe lo crea

    Args:
        filename (texto): archivo donde se escribira. Defaults to ""
        text (str): texto que se escribira en filename. Defaults to "".
    """
    with open(filename, 'w', encoding='utf-8') as fd:
        x = fd.write(text)
        print(x)

write_file("/home/klich1984/holbeton/Tests/examples_json/my_first_file.txt", "Hola klich\n")