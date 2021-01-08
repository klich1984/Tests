class moto():
    """Calss moto

    Raises:
        TypeError: error of type of the variable

    Returns:
        [type]: [description]
    """
    chasis = 100
    llantas = 2

    def __init__(self, cilindraje, tipo, marca, color):
        """atributos de la clase motos """
        self.cilindraje = cilindraje
        self.tipo = tipo
        self.marca = marca
        self.color = color
        self.tanque = "vacio"

    @property
    def cilindraje(self):
        return self.__cilindraje

    @cilindraje.setter
    def cilindraje(self, value):
        if type(value) != int:
            raise TypeError("solo numeros")
        self.__cilindraje = value

    def tanquiar(self, llenar):
        if llenar == True:
            self.tanque = "lleno"

    def informacion(self):
        print("estas son propiedades de la moto marca: {}\n\
        cilindraje   {}cc\n\
        llantas      {}\n\
        tipo         {}\n\
        chasis       {}\n\
        color        {}\n\
        tanque       {} "\
        .format(self.marca, self.cilindraje, self.llantas, self.tipo, self.chasis, self.color, self.tanque))


motolaura = moto(135, "sport", "yamaha", "morado")
motocarlos = moto(750, "turnin", "susuki", "azul")
motolaura.informacion()
motolaura.cilindraje = "bajo"
motolaura.tanquiar(True)
motolaura.informacion()