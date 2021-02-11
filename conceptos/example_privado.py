#!/usr/bin/python3

class Demo:
    def __secret(self):
        print('Nadie puede saber!')

    def public(self):
        self.__secret()

class Child(Demo):
    def __secret(self):
        print('No puedo contarte!')


demo = Demo()
demo.__secret()
demo.public()
child = Child()
child.public()

print(dir(demo))
