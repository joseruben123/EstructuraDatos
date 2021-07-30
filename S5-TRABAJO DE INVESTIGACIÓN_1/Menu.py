import os
num1=10
num2=5
while True:
    print(f"Menu de opciones - Que deseas hacer hoy? : Tienes {num1} y {num2}\n\
        1. para multiplicar.\n\
        2. para dividir.\n\
        3. para sumar.\n\
        4. para restar.\n\
        5. para salir.")
    opcion=input()
    if opcion=='1':
        print(f"Este es el resultado de la multiplicacion {num1*num2}")
    elif opcion=='2':
        print(f"Este es el resultado de la divicion {num1/num2}")
    elif opcion=='3':
        print(f"Este es el resultado de la suma {num1+num2}")
    elif opcion=='4':
        print(f"Este es el resultado de la resta {num1-num2}")
    elif opcion=='5':
        break
    input()
    os.system("cls")