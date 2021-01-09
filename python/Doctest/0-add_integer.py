#!/usr/bin/python3
"""suma dos enteros"""


def palindromo(palabra):
    """Comprueba si una palabra es un palíndrimo. Los palíndromos son
    palabras o frases que se leen igual de ambos lados.
    Si es un palíndromo devuelve True y si no False

    >>> palindromo("radar")
    True

    >>> palindromo("somos")
    True

    >>> palindromo("holah")
    False

    >>> palindromo("Ana")
    True

    >>> palindromo("Atar a la rata")
    True
    """
    if palabra.lower().replace(" ", "") == palabra[::-1].lower().replace(" ", ""):
        return True
    else:
        return False

if __name__ == "__main__":
    import doctest
    doctest.testmod()
