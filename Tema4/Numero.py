from abc import abstractmethod
from abc import ABCMeta


class Numero(metaclass=ABCMeta):
    _cifra = int(0)

    @abstractmethod
    def calcularCifra(self):
        pass

    @abstractmethod
    def getCifra(self):
        pass
