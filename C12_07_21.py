class Ordenar:
    def _init_(self,lista):
        self.lista=lista
    def borbuja(self):
        for i in range(len(self.lista)):
            for j in range(i+1,len(self.lista)):
                if self.lista[i] > self.lista[j]:
                    aux = self.lista[i]
                    self.lista[i]=self.lista[j]
                    self.lista[j]=aux
    def insertar(self,valor):
        self.borbuja()
        auxilista=[]
        enc= False
        for pos,ele in enumerate(self.lista):
            if ele > valor:
                enc=True
                break
        if enc:self.lista = self.lista[0:pos]+ auxilista + self.lista
        else: self.lista.append(valor)
        return self.lista

    def insertar2(self,valor):
        self.borbuja()
        auxlista=[]
        enc=False
        for pos,ele in enumerate(self.lista):
            if ele > valor:
                auxlista.append(valor)
                enc=True
                break
        if enc: 
            for i in range(pos):
                auxlista.append(self.lista[i])
            auxlista.append(valor)
            for j in range(pos,len(self.lista)):
                auxlista.append(self.lista[j])
        else:
             self.lista.append(valor)
        return self.lista

ord1 = Ordenar([10,15,20,70,80])
#                   0  1  2  3  4
#                             pos

print(ord1.insertar(5))

##herencia 
class Persona:
    _siguiente = 0
    def __init__(self,nombre="invitado", activo= True):
        self.__codigo = self._siguiente()
        self.__nombre = self.__nombreMayuscula(nombre)
        self.activo= activo

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,nom):
        self._nombre = nom
    @property
    def codigo(self):
        return self.__codigo
    @codigo.setter
    def codigo(self,cod):
        self.__codigo = cod

    def siguiente(Self):
        Persona._siguiente = Persona._siguiente+1
        return Persona._siguiente

    def __nombreMayuscula(self,nomb):
        return nomb.upper()

    def mostrar_datos(self):
        return "Codigo: {} - Nombre: {} - Activo: {}".format(self)

class Empleado(Persona):

    def __init__(self,nom = "invitado",act=True, sueldo=400):
        Persona.__init__(self,nom,act)
        self.sueldo = sueldo 
    
    def mostrar_datos(self):
        return Persona.mostrar_datos(self) +" -sueldo: "+ str(self)