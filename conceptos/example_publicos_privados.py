#!/usr/bin/python3

class Circulo:
    pi = 3.1415   # Atributo de clase

class User:
    def __init__(self, username):
        self.username = username

    def set_username(self, username):
        self.username = username

    def get_username(self):
        return self.username

print("pi =", Circulo.pi)
cody = User("Cody")
print(cody.username)
# Cambiar contenido de username
cody.username = "klich84"
print(cody.username)
