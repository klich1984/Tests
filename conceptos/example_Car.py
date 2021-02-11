#!/usr/bin/python3

class Car:
    wheels = 0
    def __init__(self, color, model, year):
        self.color = color
        self.model = model
        self.year = year
        self._cupholders = 6

my_car = Car('Yellow', 'beetle', 1967)
my_new_car = Car('red', 'corvette', 1999)
print(f'My car is {my_car.color}')
print(f'My nw car is {my_new_car.color}')
# modifico el vatributo wheels de la clase
Car.wheels = 5
print(f'wheels class: {Car.wheels}')
# modifico el atributo de la instancia my_car no se modifica la de la clase
my_car.wheels = 4
my_new_car.wheels = 8
Car.wheels = 20
print(f'wheels my_car: {my_car.wheels}')
print(f'wheels class: {Car.wheels}')
print(f'wheels my_new_car: {my_new_car.wheels}')
#accediento al atributo NO PUBLICO _cupholders
print(f'It has {my_car._cupholders} cupholders.')



