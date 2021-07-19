class Logica:

    def __init__(self, lista=None):
        self.__lista = lista

    @property
    def lista(self):
        return self.__lista
    @lista.setter
    def lista(self, value):
        self.__lista = value

    def parImpar(self, numero):
        rec = numero % 2
        if rec == 0:
            print("{} es par", format(numero))
        else:
            print("{} es Imprtar".format(numero))

    def perfecto(self, num):
        acu = 0
        for contador in range(1, num):
            rec = num % contador
            if rec == 0:
                acu = acu + contador
        if acu == num:
            print("{} es perfecto".format(num))
        else:
            print("{} no es perfecto".format(num))


class Ejer(Logica):
    def __init__(self, lista, numeros):
        super().__init__(lista)
        self.dato = numeros

    def sumar(self, n1, n2):
        return n1 + n2

    def parImpar(self, numero):
        super().parImpar(numero)
        return numero % 2

ej = Ejer([1, 3, 5],20)
ej.perfecto(6)
# ejer.parImpar()
# print(ejer.sumar(4,8))