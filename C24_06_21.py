####ejercicios de deber
class Tarea:
    def __init__(self):
        pass

    def pagoJornadaExtra(self):
        horastrabajadas,horasextras,horasextratriple =0,0,0
        valorHora , pagohorasextra, pagototal=0,0,0
        horastrabajadas=int(input("Ingrese horas trabajadas: "))
        valorHora=float(input("Ingresar valor hora: "))
        if horastrabajadas>40:
            horasextras=horastrabajadas-40
            if horasextras>8:
                horasextratriple=horasextras-8
                pagohorasextra=valorHora*2*8+valorHora*3*horasextratriple
            else:
                pagohorasextra=valorHora*2*horasextras
            pagototal=valorHora*40+pagohorasextra
        else:
            pagototal=valorHora*horastrabajadas
        print("Horas trabajadas: {}, horas extras: {}, horas triples: {}, valor hora: {}, pago extra: {}, pago total: {}".format(horastrabajadas,horasextras,horasextratriple,valorHora,pagohorasextra,pagototal))

    def mayor(self):
        n1,n2,n3=0,0,0
        n1=int(input("Ingrese numero 1: "))
        n2=int(input("Ingrese numero 2: "))
        n3=int(input("Ingrese numero 3: "))
        if n1>n2>n3:
            print(n1)
        elif n2>n1>n3:
            print(n2)
        else:
            print(n3)


tarea=Tarea()
tarea.pagoJornadaExtra()
tarea.mayor()