#Libreria sleep()

import os
from time import sleep

# Arqueo de Caja - Designed by Gian Carlo

# Funciones

def menu ():
    opcion = 0
    while opcion == "8":
        print("Usted ha elegido salir del programa!")
        
    billetesde_10 = 10
    billetesde_20 = 20
    billetesde_50 = 50
    billetesde_100 = 100
    billetesde_200 = 200
    billetesde_500 = 500
    billetesde_1000 = 1000
    monto_total_caja = 0
    monto_total_sistema = 0
    
    print("Bienvenido al menu de Arqueo de Caja")
    print("Eliga una de las opciones para ingresar la cantidad de billetes")
    print("para poder evaluar cuanto dinero hay en la caja"),sleep(3)
    monto_total_sistema = input("Ingrese el total de dinero que marca el sistema: ")
    print("1. Billetes de $10"),sleep(1)
    print("2. Billetes de $20"),sleep(1)
    print("3. Billetes de $50"),sleep(1)
    print("4. Billetes de $100"),sleep(1)
    print("5. Billetes de $200"),sleep(1)
    print("6. Billetes de $500"),sleep(1)
    print("7. Billetes de $1000"),sleep(1)
    print("8. Salir.")
    
    opcion = input("Eliga unas de las opciones para poder seguir.")
    if opcion == "1":
        billetesde_10 * input("¿Cuantos billetes de $10?: ")
    elif opcion == "2":
        billetesde_20 * input("¿Cuantos billetes de $20?: ")
    elif opcion == "3":
        billetesde_50 * input("¿Cuantos billetes de $50?: ")
    elif opcion == "4":
        billetesde_100 * input("¿Cuantos billetes de $100?: ")
    elif opcion == "5":
        billetesde_200 * input("¿Cuantos billetes de $200?: ")
    elif opcion == "6":
        billetesde_500 * input("¿Cuantos billetes de $500?: ")
    elif opcion == "7":
        billetesde_1000 * input("¿Cuantos billetes de $1000?: ")
        
    monto_total_caja = billetesde_10+billetesde_20+billetesde_50+billetesde_100+billetesde_200+billetesde_500+billetesde_1000
    
    
menu()





