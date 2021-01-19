#!/usr/bin/python3
#Clase Padre, Base, Principal, o Superclase
class Triangle:
    #constructor
    def __init__(self):
        print("Calculo de las partes de un triangulo")
    #método area
    def area(self, base, altura):
        self.base = base
        self.altura = altura
        return (base * altura) / 2
    #método base
    def base(self, area, altura):
        self.area = area
        self.altura = altura
        return (area * 2) / altura
    #metodo altura
    def altura(self, area, base):
        self.area = area
        self.base = base
        return (area * 2) / base
#Creacionde clase hija que hereda a la clase padre Triangle, se introduce entre parentesis
class Trapecio_Regular(Triangle):
    #constructor
    def __init__(self):
        print("Calculo del área de un trapecio regular")
    #método altura de la clase hija que llama al método altura de la clase padre mediante
    #super.altura()
    def altura(self):
        super.altura(area, base)
    #método propio llamado area igual que en el padre pero que se correra aca
    def area(self, base_mayor, base_menor, altura):
        return ((base_mayor + base_menor) * altura / 2)

t1 = Triangle()
#probamos el funcionamoento de la clase padre
print(t1)
#llamaos al metodo que despues vamos a invocar en la clase hija
print(t1.altura(4, 4))
#Creamos instancia/objeto a Trapecio_regular
a = Trapecio_Regular()
#llamada a la clase hija
print(a)
#Introducimos los argumentos requeridos por el método, pasamos la altura como no lo piede la clase Padre
print(a.area(10, 5, t1.altura(4, 4)))
