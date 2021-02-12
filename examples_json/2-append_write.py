#!/usr/bin/python3
"""  Agrega texto a uno ya creadosi el archivo no existe debe ser creado """

def append_write(filename="", text=""):
    """agrega texto al archivo pasado

    Args:
        filename (str): Archivo donde escribiremos. Defaults to "".
        text (str): texto que sera copiado. Defaults to "".
    """
    with open(filename, 'a', encoding='utf-8') as fd:
        x = fd.write(text)
        print(x)

# Si se le coloca salto de linea al final lo guarda y la siguiente llamada se copiara en la siguiente linea
append_write("/home/klich1984/holbeton/Tests/examples_json/file_append.txt", "Linea 5\n")