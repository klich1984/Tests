#crear clase padreo o superclase
class Vehiculos():
    #creamos constructor
    def __init__(self, marca, modelo):
        #Damos un estado inicial a los objetos que hereden

        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    #Creamos los comportamientos (Metodos)
    #Creamos metodo arrancar
    def arrancar(self):

        self.enmarcha = True

    #Creamos metodo acelerar
    def acelerar(self):

        self.acelera = True

    #Creamos metodo frenar
    def frenar(self):

        self.frena = True

    #Creamos metodo estado
    def estado(self):
        print("Marca:", self.marca, "\nModelo:", self.modelo, "\nEl marcha:", self.enmarcha,
            "\nAcelerando:", self.acelera, "\nFrenando:", self.frena)

#Crear clase que hereda a vehiculo, la clase moto hereda a vehiculo
class Moto(Vehiculos):
    pass

#Crear objeto, se le deben pasar los parametros que tiene el constructor ya que la heredamos
miMoto = Moto("Honda", "CBR")

#Podemos llamar a cualquer instancia que se han heredado
miMoto.estado()