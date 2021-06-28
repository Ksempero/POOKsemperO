#Kevin Javier Semper Ordonez
#Ejercicio POO

class Ejercicios:
    def __init__(self):
        pass
    
    #EJERCICIO1.diseñamos un pseudocódigo para encontrar la superficie de un círculo para un radio 
    def calculo(self):
        R = float(input("ingrese el radio: "))
        p = 3.1416
        s = p*R**2
        print("la superficie de su circulo es:{} ".format(s))

    #EJERCICIO2.En una tienda se ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuánto deberá pagar finalmente por su compra
    def descuento(self):
        TCompra = float(input("Valor total de la compra: "))
        Desc = TCompra*0.15
        TPagar = TCompra-Desc
        print("Su total a cancelar es: {} ".format(TPagar))

    #EJERCICIO3.Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas El vendedor desea saber cuánto dinero obtendrá por concepto de comisiones por 
    # Estas ventas se deben realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y sus comisiones.
    def ventas(self):
        for x  in range(4):
            Sueldo = float(input("Ingrese su salario: "))
            ve1 = float(input("valor de la primer venta: "))
            ve2 = float(input("valor de la segunda venta: "))
            ve3 = float(input("valor de la tercera  venta: "))
            TotalV = ve1+ve2+ve3
            Com = TotalV*0.1
            Tv = round(TotalV+Com,2) 
            print("El total a recibir por comicion es:{} ".format(Tv))

    #EJERCICIO4.Construir un algoritmo tal, que dado como dato la calificación de un alumno en un examen, escriba
    def algoritmo(self):
        Calificacion = float(input("Ingresar la calificacion: "))
        if Calificacion >= 7:
            print("Has aprobado ")
        
    #JERCICIO 5. Dado como dato la calificación de un alumno en un examen, escriba “aprobado” si su calificación es mayor o igual que 7 y “Reprobado” en caso contrario.
    def algoritmo2(self):
        Cali = float(input("Ingrese su calificacion: "))
        if Cali >= 7:
            print("Has aprobado ")
        else:
            print("Has reprobado")

    #EJERCICIO6.Dado el sueldo de un empleado, encontrar el nuevo sueldo si obtiene un aumento del 10% si su sueldo es inferior a $600, en caso contrario no tendrá aumento.
    def sueldo(self):
        salario = float(input("Ingrese su sueldo: "))
        if salario < 600:
            n = salario+salario*0.1
            print("Su nuevo sueldo a facturar es {}".format(n))
        else:
            print("Su sueldo continua en {}".format(salario))

    #EJERCICIO7.Determinar la cantidad de dinero que recibirá un trabajador por concepto de las horas extras trabajadas en una empresa, sabiendo que cuando las horas de trabajo
    # exceden de 40, el resto  se consideran horas extras y que éstas se pagan al doble de una hora normal cuando no exceden de 8, si las horas extras sobrepasan de 8 
    # se pagan las primeras 8 al  doble de lo que se paga por una hora normal y el resto al triple.
    def dinero(self):
        Horas = int(input("horas trabjadas: "))
        P = float(input("valor a pagar por hora:$ "))
        if Horas > 48:
            tot = Horas - 48
            sld = 40*P + 8*P*2 + tot*P*3
            
        else: 
            if Horas > 40:
                Ds = Horas - 40
                sld = 40*P + Ds*P*2
            else:
                sld = Horas*P
                print("El Total a pagar por las horas trabajadas es : {}".format(sld))

    
    #EJERCICIO8.Entre 3 numeros sacar cual es el mayor
    def diff(self):
        Num1 = []
        for i in range(3):
            num = float(input("Introduce el número #{}: ".format(i + 1)))
            Num1.append(num)
        m = Num1[0]
        for num in Num1:
            if num > m:
                m = num
        print("El numero mayor es : {}".format(m))

    #EJERCICIO9.Diseñar un algoritmo donde ingresen dos variables de tipo entero, obtenga el resultado de la siguiente función:
    def var(self):
        vlr = int(input("Ingrese el valor: "))
        num = int(input("Ingrese el valor de num: "))
        if num == 1:
            rtd = 100*vlr
        elif num == 2:
            rtd = 100^vlr
        elif num == 3:
            rtd = 100/vlr
        else:
            rtd = 0
        print("El resultado es {}".format(rtd)) 

    #EJERCICIO10.Una escuela aplica dos exámenes a sus aspirantes, por lo que cada uno de ellos obtiene dos calificaciones denotadas como C1 y C2. El aspirante que obtenga 
    #calificaciones mayores que 80 en ambos exámenes es aceptado; en caso contrario es rechazado
    def exa(self):
        C1 =int(input("Ingrese la nota C1 "))
        C2 = int(input("Ingrese la nota C2: "))
        if C1 >= 80 and C2 >= 80:
            print("Felicidades, aceptado")
        else:
            print("Rechazado")

    #EJERCICIO11.Calcular la suma de los cuadrados de los primeros 100 enteros y escribir el resultado
    def cuadrados(self):
        Sm = 0
        i = 1
        for i  in range(101):
            Sm = Sm + i
            i += 1
        print(Sm)
    #JEJERCICIO2.Elabore pseudocódigo para escribir los números del 1 al 100
    def num(self):
        i = 0
        while i<100:   
            i += 1
            print(i)
    #EJERCICIO13.Calcular la suma y producto de números enteros, utilizando un bucle controlado por el usuario
    def buc(self):
        summ = 0
        pii = 1
        nii = "y"
        while nii != "nii"and nii != "N":
            num = int(input("Ingrese el valor: "))
            summ += num
            pii *= num
            nii = input("Desea continuar(S/N)" )

        print("Total de la suma es :{}".format(pii))
        print("total del producto es :{}".format(summ))

    #EJERCICIO14.calcular la suma y producto de N números enteros, utilizando un bucle controlado por centinela
    def calc(self):
        summa = 0
        p = 1
        n = int(input("Ingrese el valor: "))
        while n != -1:
            summa += 1
            p = p*n            
        print("Total de la suma es :{}".format(p))
        print("total del producto es :{}".format(summa))

    #EJERCICIO15.Determinar si un número entero ingresado por el usuario es primo. Un número primo es un entero que no tiene más divisores que él mismo y la unidad.
    def pri(self):
        primo = "True"
        div = 2
        r = int(input("Ingrese su numero:"))
        while div < r and primo == "True":
            res = r % div
            if res == 0:
                primo = "False"
                div = div+1
        if primo == "True":
            print("Su numero {} es primo " .format(r))
        else:
            print("Su numero {} no es primo".format(r))

    #EJERCICIO16.Aplicar los pasos de la metodología para la solución de un problema para leer un número entero N y calcular el resultado de la siguiente serie:
    #1 – 1/2+ 1/3 – 1/4 +.... +/- 1/N. Resolveremos el problema utilizando bucle Repeat controlado por contador y usando banderas.
    def metodo(self):
        from fractions import Fraction
        ser = 0
        Inc = 1
        VE = int(input("Ingrese un numero entero: "))
        b = "T"
        for x in range (VE):
            if b == "T":
                ser = ser + Fraction(1,Inc)
                b ="F"               
            else:
                ser = ser - Fraction(1,Inc)
                b = "T"
            Inc += 1           
        print(ser) 
    #EJERCICIO17.Calcular el factorial de N números enteros leídos de teclado.
    def fac(self):
        num = int(input('Intreoducir Rango: '))
        for i in range(1,num+1):
            m = int(input('Introducir Numero: '))
            fact = 1
        for j in range(1,m+1):
            fact = fact * j
            print(f'El factorial es: {fact}')
    #EJERCICIO18.Aplicar las fases  para  la resolución de un problema para leer un vector de 20 números enteros y a continuación escribir en un vector A todos los números
    #negativos y en un vector B todos los positivos o iguales a cero. Imprimir dichos vectores
    def vector(self):
        import random as rd
        promd = []
        calcl = [[rd.randint(0,10)for e in range(6)]for e in range(30)]
        for i in range(30):
            sum = 0
            for j in range(6):
                sum = sum + calcl[i][j]
                pd = round(sum/6,2)
            promd.append(pd)
            print(f'promedio del alumno: {i+1} : {round(sum/6,2)}')

        promd.sort(reverse=True)
        print(f'La mayor nota es: {promd[0]}')







        





    















           

          
            
            



        

cal1 = Ejercicios()
cal1.vector()


