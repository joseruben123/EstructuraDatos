import os
from calculadora import CalEstandar, CalCientifica

class Menu:
    def __init__(self,titulo,opciones=[]):
        self.titulo=titulo
        self.opciones=opciones
    def menu(self):
        print(self.titulo)
        for opcion in self.opciones:
            print(opcion)
        opc=input("elijaopcion[1...{}]: ".format(len(self.opciones)))
        return opc
opc=""   
while opc !=5:
    os.system("cls")
    menu=Menu("Menu Principal",["1) Calculadora", "2) Numeros", "3)Listas ", "4) Cadenas","5) Salir"])
    opc=men.menu()
    if opc=="1":
        opc1=""
        while opc1 !="4":
            os.system("cls")
            men1=Menu("Menu Calculadora",["1) Sumaa", "2) Resta", "3)Multiplicacion ", "4) Divisor","5) Salir"])
            opc1=men1.menu()
            if opc1=="1":
                print("Suma de dos nuemros")
                n1=int(input("Ingrese numero1: "))
                n2=int(input("Ingrese numero2: "))
                print(n1+n2)
                cal=CalEstandar(n1.n2)
                print(cal.suma())
                input("Presione una tecla para continuar....")
            
            elif opc1=="2":
                print("Resta de dos nuemros")
            
            elif opc1=="3":
                print("Multiplicacion de dos nuemros")
                n1=int(input("Ingrese numero1: "))
                n2=int(input("Ingrese numero2: "))
                cal=CalEstandar(n1.n2)
                print(cal.multiplicacion())
        
    elif opc=="2":
        men2=Menu("Menu Numeros",["1) Perfecto", "2) Primo", "3)Salir "])
        opc2=men2.menu()
        
        if opc2=="1":
            print("Numeros Perfectos")
            num=int(input("Ingrese numero: "))
            print("El numero es perfecto")
    
    elif opc=="3":
        print("Listas")
        
        
    elif opc=="4":
        print("Cadenas")