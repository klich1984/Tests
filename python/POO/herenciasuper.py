class Persona():

    def __init__(self, nombre, edad, lugar_residencia):

        self.nombre = nombre
        self.edad = edad
        self.lugar_residencia = lugar_residencia

    def descripcion(self):

        print("Nombre:", self.nombre, "Edad:", self.edad, "residencia:", self.lugar_residencia)

class Empleado(Persona):

    def __init__(self, salario, antiguedad):

        super().__init__("Carlos", 37, "colombia")

        self.salario = salario
        self.antiguedad = antiguedad

print("------------Antonio-------------")

Antonio = Persona("Antonio", 55, "España")

Antonio.descripcion()

print("------------Carlos-------------")

Carlos = Empleado(1500, 15)

Carlos.descripcion()