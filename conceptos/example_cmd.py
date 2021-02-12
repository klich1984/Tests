#!/usr/bin/python3

try:
    import gnureadline
    import sys
    sys.modules['readline'] = gnureadline
except ImportError:
    pass

import cmd

class HelloWorld(cmd.Cmd):
    intro = 'Bienvenido a cmd'
    prompt = '--> '
    file = None

    def do_saludar(self, persona):
        """ Saluda [Persona] """
        if persona: #Si persona existe
            print('Hola', persona)
        else:
            print('Hola')

    def help_saludar(self):
        print('\n'.join([
            'Saludar [persona]',
            'Saluda a la persona nombrada',
        ]))

    def do_fin(self, line):
        return True

if __name__ == '__main__':
    HelloWorld().cmdloop()
