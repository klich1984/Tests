class Coche():
    #Propiedades del coche
    largochasis = 250
    anchochasis = 120
    ruedas = 4
    enmarcha = False

    def arrancar(self, arrancamos):
        self.enmarcha = arrancamos

        if(self.enmarcha):
            return "El coche esta en marcha"
        else:
            return "El coche esta parado"

    def estado(self):
        print("El coche tiene ", self.ruedas, "ruedas, Un ancho de ", self.anchochasis, "y un largo de ",
            self.largochasis)

miCoche = Coche()
print(miCoche.arrancar(True))

miCoche.estado()

print("------------A continuacion creamos el segundo objeto --------------")

miCoche2 = Coche()
print(miCoche2.arrancar(False))
miCoche2.estado()
