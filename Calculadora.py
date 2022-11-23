# Funciones.

import os
from time import sleep

from colorama import Fore, Back, Style

# Suma

def s (a,b):
    return (a+b)

# Resta

def r (a,b):
    return (a-b)

# Multiplicacion

def m (a,b):
    return (a*b)

# Division

def d (a,b):
    return (a/b)

# Potenciacion

def p (a,b):
    return (a**b)

def mm ():
    print(Style.BRIGHT +"Menu de Calculadora - Designed by Jhon Cross")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Potenciacion")
    print("6. Salir")
    menu = input("Elige una de las opciones con su respectivo numero: ")
    return menu 

def i ():
    a=float(input("Valor del primer numero?: "))
    b=float(input("Valor del segundo numero?: "))
    return(a,b)

opcion = "0"

while opcion != "6":
    opcion = mm() 


    if opcion == "1":
        a,b=i()
        print("La suma de estos numeros es : " +str(s(a,b))),sleep(2),os.system('clear')

    elif opcion == "2":
        a,b=i()
        print("La resta de estos numeros es : " +str(r(a,b))),sleep(2),os.system('clear')

    elif opcion == "3":
        a,b=i()
        print("La multiplicacion de estos numeros es : " +str(m(a,b))),sleep(2),os.system('clear')
        
    elif opcion == "4":
        a,b=i()
        print("La division de estos numeros es : " +str(d(a,b))),sleep(2),os.system('clear')

    elif opcion == "5":
        a,b=i()
        print("La potenciacion de estos numeros es : " +str(p(a,b))),sleep(2),os.system('clear')

    elif opcion == "6":
        print("Usted a elegido salir, nos vemos."),sleep(2),os.system('clear')
        

    



