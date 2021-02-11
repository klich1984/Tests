#!/usr/bin/python3

import cmd

class HelloWorld(cmd.Cmd):
    intro = 'Bienvenido a cmd'
    prompt = '--> '
    file = None

    def do_saludar(self, line):
        print('Hola Mundo')

    def do_fin(self, line):
        return True

if __name__ == '__main__':
    HelloWorld().cmdloop()
