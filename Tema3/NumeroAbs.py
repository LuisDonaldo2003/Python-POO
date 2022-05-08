from abc import ABC

class NumeroAbs(ABC):

    @staticmethod #No se ocupa el self en abstracta
    def Cantidad(cifra):
        totalDigito = 0
        if cifra == 0 or cifra < 10:
            totalDigito = 1
        elif cifra == 10 or cifra < 100:
            totalDigito = 2
        elif cifra == 100 or cifra < 1000:
            totalDigito = 3
        elif cifra == 1000 or cifra < 10000:
            totalDigito = 4

        return totalDigito
