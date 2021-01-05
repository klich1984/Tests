class Coche():
    #Propiedades del coche
    largochasis = 250
    anchochasis = 120
    ruedas = 4
    enmarcha = False

    def arrancar(self):
        self.enmarcha = True

    def estado(self):
        if(self.enmarcha):
            return "El coche esta en marcha"
        else:
            return "El coche esta parado"

miCoche = Coche()
print("El largo del coche es: ", miCoche.largochasis)
print("El coche tiene", miCoche.ruedas, "ruedas")

miCoche.arrancar()
print(miCoche.estado)
print("------------A continuacion creamos el segundo objeto --------------")

miCoche2 = Coche()
print("El largo del coche es: ", miCoche2.largochasis)
print("El coche tiene", miCoche2.ruedas, "ruedas")
print(miCoche2.estado)
