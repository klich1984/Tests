#!/usr/bin/python3

class Car:
    wheels = 0
    def __init__(self, color, model, year):
        self.color = color
        self.model = model
        self.year = year
        self._voltage = 12

    @property
    def voltage(self):
        return self._voltage

    @voltage.setter
    def voltage(self, volts):
        print('Advertencia: !esto puede causar problemas!')
        self._voltage = volts

    @voltage.deleter
    def voltage(self):
        print('Advertencia: ¡la radio dejará de funcionar!')
        del self._voltage

my_car = Car('Yellow', 'beetle', 1967)
print(f'My car uses {my_car.voltage} volts')
my_car.voltage = 6
print(f'My car now uses {my_car.voltage} volts')
del my_car.voltage