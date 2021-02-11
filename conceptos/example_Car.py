#!/usr/bin/python3

class Car:
    wheels = 0
    def __init__(self, color, model, year):
        self.color = color
        self.model = model
        self.year = year

my_car = Car('Yellow', 'beetle', 1967)
print(f'My car is {my_car.color}')
# Ingreso un nuevo atributo a my_car llamado wheels
my_car.wheels = 5
print(f'wheels: {my_car.wheels}')
# print(dir(my_car))
print(f'wheels: {Car.wheels}')


