#!/usr/bin/python3
"""  Funcion que escribe un objeto a un archivo de texto en representacion json """
import json


def save_to_json_file(my_obj, filename):
    """Crea un archivo(filename) de texto con representacion json con el objeto pasado

    Args:
        my_obj (objeto): Objeto que sera convertido a texto en representacion json
        filename (str): string que sera el nombre del archivo donde se guardara el objeto
    """
    #x = json.dumps(my_obj)  #Me convierte el objeto en un string (representacion json)
    with open(filename, 'w', encoding='utf-8') as fd:
        fd.write(json.dumps(my_obj))

filename = "/home/klich1984/holbeton/Tests/examples_json/my_list.json"
my_list = [1, 2, 3]
save_to_json_file(my_list, filename)

filename = "/home/klich1984/holbeton/Tests/examples_json/my_dict.json"
my_dict = { 
    'id': 12,
    'name': "John",
    'places': [ "San Francisco", "Tokyo" ],
    'is_active': True,
    'info': {
        'age': 36,
        'average': 3.14
    }
}
save_to_json_file(my_dict, filename)

try:
    filename = "/home/klich1984/holbeton/Tests/examples_json/my_set.json"
    my_set = { 132, 3 }
    save_to_json_file(my_set, filename)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))