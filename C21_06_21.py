from Clase21 import Cargo
class Empleado:
    codigo=0
    def __init__(self,nom,ced,sue,Clase21):
        self.codigo=self.generarCodigo()
        self.nombre=nom
        self.cedula=ced
        self.sueldo=sue
        self.cargo=Clase21

    def mostrar(self):
        print("codigo: {} nombre: {} cargo:{}-{}".format(self.codigo,self.nombre, self.cargo.codigo, self.cargo.descripcion))

    def generarCodigo(self):
        Empleado.codigo= Empleado.codigo+1
        return Empleado.codigo

# x=5
# nom="Ana"
cargo1=Cargo("Docente")
emp1=Empleado("Kevin Semper","0963197077",600,cargo1)
emp1.mostrar()
cargo2=Cargo("Analista")
emp2=Empleado("Carolina","095564337",450,cargo2)
emp2.mostrar()