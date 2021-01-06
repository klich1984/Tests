"""03 Crear una clase que tenga caracteristicas propias
Tiene un cosntructor
implementacion de class VehiculoEL y BicicletaElectrica
herencia multiple"""

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
        print("Marca:", self.marca, "\nModelo:", self.modelo, "\nEn marcha:", self.enmarcha,
            "\nAcelerando:", self.acelera, "\nFrenando:", self.frena)

#Crear clase que hereda a Vehiculo, la clase Furgoneta hereda a Vehiculo
class Furgoneta(Vehiculos):

    #Creamos metodo carga con un parametro adicional cargar
    def carga(self, cargar):
        self.cargado = cargar
        #Si cargado es igual a True (Es verdadero)
        if(self.cargado):
            return "La furgoneta esta cargada"
        else:
            return "La furgoneta no esta cargada"


#Crear clase que hereda a vehiculo, la clase moto hereda a Vehiculo
class Moto(Vehiculos):
    """Esta clase tuene 6 metodos, 5 heredados d vehiculos y 1 propio = caballito"""
    #Creo una variable
    hcaballito = ""
    #Creo un metodo
    def caballito(self):
        self.hcaballito = "Voy haciendo el caballito"

    #Creamos metodo estado igual al heredado
    def estado(self):
        print("Marca:", self.marca, "\nModelo:", self.modelo, "\nEn marcha:", self.enmarcha,
            "\nAcelerando:", self.acelera, "\nFrenando:", self.frena, "\n", self.hcaballito)

#creamos objeto llamado VElectricos
class VElectricos():
    #Creamos un constructor para esta clase
    def __init__(self):
        self.autonomia = 100

    def cargarEnergia(self):

        self.cagando = True

print("--------Objeto miMoto------------")
#Crear objeto, se le deben pasar los parametros que tiene el constructor ya que la heredamos
miMoto = Moto("Honda", "CBR")

#LLamamos a un metodo propio de la clase Moto
"""de esta manera miMoto.caballito() no nos muestra nada en a salida ya que al llamar miMoto.estado()
estamos llamando a la clase vehiculo para hacerlo lo que se hace es crear un metodo que se llame
exactamene igual al heredado y con la misma cantidad de argumentos"""
miMoto.caballito()

#Podemos llamar a cualquer instancia/metodo que se han heredado
miMoto.estado()

print("--------Objeto miFurgoneta------------")
#Creamos objeto
miFurgoneta = Furgoneta("Renault", "Kango")
#Podemos llamar a cualquer instancia/metodo que se han heredado
miFurgoneta.arrancar()
miFurgoneta.estado()
#debemos meterlo en un print ya que la clase esta retornando un string
print(miFurgoneta.carga(True))

print("--------Objeto miBici------------")
#Creamos clase BicicletaElectrica que hereda todos los metodos de VElectricos y de Vehiculos
#OJO tomara el constructor de la primera clase que le pasamos como herencia
class BicicletaElectrica(VElectricos, Vehiculos):
    pass

#Creamos un Objeto miBici
miBici = BicicletaElectrica()
