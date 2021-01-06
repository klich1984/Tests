"""Princiio de sustitucion
es siempre un/a para verificar si esta bien diseñado
para esto usamos isinsta
isinsta devuelve True si pertenece o False si no
Una empleado es un persona
"""
class Persona():

    def __init__(self, nombre, edad, lugar_residencia):

        self.nombre = nombre
        self.edad = edad
        self.lugar_residencia = lugar_residencia

    def descripcion(self):

        print("Nombre:", self.nombre, "Edad:", self.edad, "residencia:", self.lugar_residencia)

class Empleado(Persona):

    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):

        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)

        self.salario = salario
        self.antiguedad = antiguedad

    def descripcion(self):

        super().descripcion()

        print("Salario:", self.salario, "Antiguedad:", self.antiguedad)

print("------------Antonio-------------")

Antonio = Persona("Antonio", 55, "España")

Antonio.descripcion()
print(isinstance(Antonio, Empleado))
print(isinstance(Antonio, Persona))

print("------------Carlos-------------")

Carlos = Empleado(1500, 15, "Carlos", 37, "Colombia")

Carlos.descripcion()

print(isinstance(Carlos, Empleado))
print(isinstance(Carlos, Persona))