from Numero import *
from NumeroAbs import *


if __name__ == '__main__':

    print("Metodos de la clase de Instancia.")
    prueba = Numero(144)
    print(prueba.get_prueba())

    print("Metodos de la clase Abstracta.")
    print(NumeroAbs.Cantidad(98))
