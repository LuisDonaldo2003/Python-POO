from abc import ABCMeta

class Digitos(ABCMeta):

    @staticmethod
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

class pruebaArchivo:
    def leerArchivo(self, archivo):
        file = open(archivo, 'r')
        lineas = []
        lineas_archivo = []
        for linea in file.readlines():
            lineas.append(linea.replace('\n', '').split(";"))
        file.close()
        for f in range(0, len(lineas)):
            try:
                lineas_archivo.append([int(lineas[f][0])])
            except ValueError:
                lineas_archivo.append([0])
        return lineas_archivo

    def calcularDigito(self, lista):
        resultados = []
        for f in range(0, len(lista)):
            resultados.append(Digitos.Cantidad(lista[f][0]))
        return resultados

    def guardarDigito(self, entrada, resultados):
        file = open("Resultados.csv", 'w')
        file.write('Cantidad,Digito\n')
        for f in range(0, len(entrada)):
            linea = str(entrada[f][0]) + ',' + str(resultados[f]) + '\n'
            file.write(linea)
        file.close()

if __name__ == "__main__":
    prueba = pruebaArchivo()
    archivo = []
    archivo = prueba.leerArchivo("numeros.txt")
    print(archivo)
    resultado = prueba.calcularDigito(archivo)
    print(resultado)
    prueba.guardarDigito(archivo, resultado)
