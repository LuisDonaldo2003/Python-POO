from Numero import *
from NumeroAbs import *


if __name__ == '__main__':
    #Llamar a un método de clase
    print("Es un método de clase en una clase pública")
    print(Numero.calcularLaCifra(4352))

    #Llamar a un método de instancia
    print("Es un método de instancia")
    prueba = Numero(786)
    print(prueba.get_producto())

    #clase abstracta
    print("Metodos de la clase  de una clase Abstracta.")
    print(NumeroAbs.Cantidad(98))

    #Sobrecarga de operadores
    prueba2 = Numero(2)
    print("Sobrecarga de operadores(str)")
    print(str(prueba2.__str__()))
