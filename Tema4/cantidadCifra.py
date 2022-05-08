from Herencia.Numero import Numero


class cantidadCifra(Numero):
    __cifras = int(0)

    def __init__(self, cifras):
        self.__cifras = cifras
        self.calcularCifra()

    def calcularCifra(self):
        if self.__cifras == 0 or self.__cifras < 10:
            self.__cifras = 1
        elif self.__cifras == 10 or self.__cifras < 100:
            self.__cifras = 2
        elif self.__cifras == 100 or self.__cifras < 1000:
            self.__cifras = 3
        elif self.__cifras == 1000 or self.__cifras < 10000:
            self.__cifras = 4
        self._cifra = self.__cifras

    def getCifra(self):
        return self._cifra
