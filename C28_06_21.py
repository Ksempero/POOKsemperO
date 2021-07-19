class Operaciones:
    def __init__(self,num1,num2):
        self.numero1=num1
        self.numero2=num2

    def suma(self):
        suma=self.numero1+self.numero2
        return suma

    def resta(self):
        # if self.numero1>=self.numero2:
        #     return self.numero1 - self.numero2
        # return 0
        return self.numero1-self.numero2

    def multiplicacion(self):
        return self.numero1 * self.numero2

    def division(self):
        if self.numero2!=0:
            return  self.numero1 / self.numero2
        return 0

    def divisionEntero(self):
        if self.numero2 != 0:
            return self.numero1 // self.numero2
        return 0

    def residuo(self):
        return  self.numero1 % self.numero2

    def exponente(self):
        return  self.numero1 ** self.numero2

    def mostrar(self):
        print("numero 1: {} ,numero 2: {}".format(self.numero1,self.numero2))

print("Menu Operaciones Matematicas")
print("1)Suma\n 2)Resta\n 3)Multiplicacion\n 4)Division\n 5)Division Entera\n 6)Residuo\n 7)Exponente\n 8)Salir")
opc='0'
while opc!='8':
    opc = input("Elija opcion [1....8]:")
    num1 = int(input("Ingrese numero 1:"))
    num2 = int(input("Ingrese numero 2:"))
    ope = Operaciones(num1, num2)
    if opc=='1':
        print("{} + {} = {}".format(ope.numero1, ope.numero2,ope.suma()))
    elif opc=='2':
        print("{} - {} = {}".format(ope.numero1, ope.numero2,ope.resta()))
    elif opc=='3':
        print("{} * {} = {}".format(ope.numero1, ope.numero2,ope.multiplicacion()))
    elif opc=='4':
        print("{} / {} = {}".format(ope.numero1, ope.numero2,ope.division()))
    elif opc=='5':
        print("{} // {} = {}".format(ope.numero1, ope.numero2,ope.divisionEntero()))
    elif opc=='6':
        print("{} % {} = {}".format(ope.numero1, ope.numero2,ope.residuo()))
    elif opc=='7':
        print("{} ** {} = {}".format(ope.numero1, ope.numero2,ope.exponente()))

print("Gracias por su visita")