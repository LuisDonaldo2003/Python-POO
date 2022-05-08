class Numero:
    __cifra = 0
    __totalDigito = 0
    __totalesDigito = 0
    __cifras = 0

    def __init__(self, cifra):
        self.__cifra = cifra
        self.calcularCifra()

    def get_producto(self):
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



    @staticmethod
    def calcularLaCifra(cifras):
        totalesDigito = 0
        if cifras == 0 or cifras < 10:
            totalesDigito = 1
        elif cifras == 10 or cifras < 100:
            totalesDigito = 2
        elif cifras == 100 or cifras < 1000:
            totalesDigito = 3
        elif cifras == 1000 or cifras < 10000:
            totalesDigito = 4

        return totalesDigito

    def __str__(self):
        return "La cifra de esta sobrecarga es: " + str(self.__totalDigito)
