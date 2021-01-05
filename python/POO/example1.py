class Coche():
    #Propiedades del coche estado inicial
    #crear un constructor def __init__(self):
    def __init__(self):
        self.__largochasis = 250
        self.__anchochasis = 120
        #encapsular (No se puede modificar desde fuera, si desde dentro) una variable precede de __ruedas
        self.__ruedas = 4
        #importante que todas las variables encapsuladas se llamen con los __ en todo el programa
        self.__enmarcha = False

    def arrancar(self, arrancamos):
        #
        self.__enmarcha = arrancamos

        if(self.__enmarcha):
            return "El coche esta en marcha"
        else:
            return "El coche esta parado"

    def estado(self):
        print("El coche tiene ", self.__ruedas, "ruedas, Un ancho de ", self.__anchochasis, "y un largo de ",
                self.__largochasis)

miCoche = Coche()
print(miCoche.arrancar(True))

miCoche.estado()

print("------------A continuacion creamos el segundo objeto --------------")

miCoche2 = Coche()
print(miCoche2.arrancar(False))
miCoche2.estado()
