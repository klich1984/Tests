class Coche:
    #Propiedades del coche estado inicial
    #El estado inicial se realiza con un constructtor
    #crear un constructor def __init__(self):
    def __init__(self):
        #Propiedades que hacen parte de estado inicial del objeto se le antepone con self
        #encapsular (No se puede modificar desde fuera, si desde dentro) una variable precede de __ruedas
        self.__largochasis = 250
        self.__anchochasis = 120
        self.__ruedas = 4
        #importante que todas las variables encapsuladas se llamen con los __ en todo el programa
        self.__enmarcha = False

    #Creacion de metodo arrancar
    def arrancar(self, arrancamos):
        #Modificamos __enmarcha desde este metodo y no desde afuera
        self.__enmarcha = arrancamos

        #si self.__enmarcha es True
        if(self.__enmarcha):
            chequeo = self.__chequeo_interno()

        #Si el chequea == True y si chequeo == True
        if(self.__enmarcha and chequeo):
            return "El coche esta en marcha"

        elif(self.__enmarcha and chequeo == False):
            return "Algo salio mal en el chequeo, no puedes arrancar"
        else:
            return "El coche esta parado"

    #comportamientos y/o funcionalidades
    #Creacion de metodo estado
    def estado(self):
        print("El coche tiene ", self.__ruedas, "ruedas, Un ancho de ", self.__anchochasis, "y un largo de ",
                self.__largochasis)

    #Creacion de metodo chequeo_interno
    #Lo encapsulamos para que solo pueda ser usado dentro de la clase anteponiendo __
    def __chequeo_interno(self):
        print("Realizando chequeo interno")

        #creo Varibables del metodo
        self.gasolina = "ok"
        self.aceite = "ok"
        self.puertas = "cerradas"
        if (self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas"):
            return True
        else:
            return False

#Crear un objeto (instanciar una clase)
miCoche = Coche()
#Accedemos al metodo arrancar y le pasamos True selft = miCoche arrancamos recibe True
print(miCoche.arrancar(True))

miCoche.estado()

print("------------A continuacion creamos el segundo objeto --------------")

miCoche2 = Coche()
print(miCoche2.arrancar(False))
miCoche2.estado()
print(miCoche2.__chequeo_interno())
