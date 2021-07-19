class Cargo:
    codigo=0
    def __init__(self,des="Sin cargo"):
        Cargo.codigo=Cargo.codigo+1
        self.codigo=Cargo.codigo
        self.descripcion=des

if __name__=="__main__":
    cargo1=Cargo()
    # cargo1.codigo=1
    # cargo1.descripcion="Docente"
    print( cargo1.codigo, cargo1.descripcion)
    cargo2=Cargo()
    # cargo2.codigo=2
    cargo2.descripcion="Director"
    print(cargo2.codigo, cargo2.descripcion)
    cargo3=Cargo("Analista")
    print(cargo3.codigo, cargo3.descripcion)
    # print(Cargo.codigo)
    # print(Cargo1.codigo)
    # print(Cargo2.codigo)
    # print(Cargo3.codigo)