#!/usr/bin/python3
#ejemplo de herencia de propiedades
class Nombre:
    #Creacion del constructor
    def __init__(self, nombre):
        self.nombre = nombre
    def __str__(self, nombre):
        return

#creacion de una instancia/objeta a clase Nombre
n = Nombre("KLICH84")
#Declaración extendida (si a implica b y b implica c, a implica c)
x = n.nombre = "KLICH84"
print(x, str(x))

class Apellido(Nombre):
    def __init__(self, apellido):
        self.apellido = apellido
    def nomap(self, nombre, apellido):
        #Aqi invocamos la propiedad que asignamos a x
        super().__init__(self, nombre)

z = Apellido("USUGA")
y = z.apellido = "usuga"
#Ha herdado el nombre de la clase Padre nombre
print(x  + " " + y)
