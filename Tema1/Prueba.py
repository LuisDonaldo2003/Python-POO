class Prueba:
    __cifra = int(0)
    __totalDigito = int(0)

    def __init__(self,cifra):
        self.__cifra = cifra
        self.calcularCifra()

    def getTotalDigito(self):
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


if __name__ == '__main__':
    Num = Prueba(23)
    print(Num.getTotalDigito())
