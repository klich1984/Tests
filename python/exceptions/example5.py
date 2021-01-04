#!/usr/bin/python3
try:
    myFile = open("/home/klich1984/holbeton/Tests/python/exceptions/mydata.txt", encoding="utf-8")

except FileNotFoundError as ex:
    print("El Archivo no fue encontrado")
    print(ex.args)

else:
    print("File : ", myFile.read())
    myFile.close()

finally:
    print("Finalizando el trabajo")