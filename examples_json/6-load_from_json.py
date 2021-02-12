#!/usr/bin/python3
""" Funcion que crea un desde un archivo JSON """
import json


def load_from_json_file(filename):
    """crea un objeto a partir de un archivo JSON

    Args:
        filename (file.json): Archivo JSON
    """
    with open(filename, 'r', encoding='utf-8') as fd: #abrimos el archivo .json y lo guardamos en fd
        x = json.load(fd) # lo convertimos a un objeto desde un archivo por eso es load
        return x



filename = "/home/klich1984/holbeton/Tests/examples_json/my_list.json"
my_list = load_from_json_file(filename)
print(my_list)
print(type(my_list))

filename = "/home/klich1984/holbeton/Tests/examples_json/my_dict.json"
my_dict = load_from_json_file(filename)
print(my_dict)
print(type(my_dict))

try:
    filename = "/home/klich1984/holbeton/Tests/examples_json/my_set_doesnt_exist.json"
    my_set = load_from_json_file(filename)
    print(my_set)
    print(type(my_set))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    filename = "/home/klich1984/holbeton/Tests/examples_json/my_fake.json"
    my_fake = load_from_json_file(filename)
    print(my_fake)
    print(type(my_fake))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))