class Numero:
    __cifra = 0
    __totalDigito = 0

    def __init__(self, cifra):
        self.__cifra = cifra
        self.calcularCifra()

    def get_prueba(self):
        return self.__totalDigito

    def calcularCifra(self):
        if self.__cifra == 0 or self.__cifra < 10:
            self.__totalDigito = 1
        elif self.__cifra == 10 or self.__cifra < 100:
            self.__totalDigito = 2
        elif self.__cifra == 100 or self.__cifra < 1000:
            self.__totalDigito = 3
        elif self.__cifra == 1000 or self.__cifra < 10000:
            self.__totalDigito = 4
