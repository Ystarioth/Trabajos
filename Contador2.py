# Arqueo de Caja - Designed

# Libreria (Sleep)

import os
from time import sleep

# Funciones (Principales)


# Cantidad de Billetes

cant_10 = 0
cant_20 = 0
cant_50 = 0
cant_100 = 0
cant_200 = 0
cant_500 = 0
cant_1000 = 0

# Total de las Cajas
total_caja = 0
total_sistema = 0

total = 0


# Funciones (def)

print("Hola, bienvenido a la interfaz de arqueo de caja.")
print("Lo principal es poner el total que hay en el sistema.")


total_sistema = input("Ingresa el total de efectivo que marca el sistema: ")

print("Genial , ahora vamos a hacer la caja.")
print("Vamos a contar billetes , usa las opciones de abajo."),sleep(2)

def menu():
    global total
    
      

    print("**************************")
    print("1. Billetes de $10")
    print("2. Billetes de $20")
    print("3. Billetes de $50")
    print("4. Billetes de $100")
    print("5. Billetes de $200")
    print("6. Billetes de $500")
    print("7. Billetes de $1000")
    print("8. Salir")
    
    print("Total del Sistema: "+total_sistema)
    print("Total de la Caja: "+str(total))
    
    global cant_10, cant_20, cant_50, cant_100, cant_200,cant_500,cant_1000    
    opcion = input("Elige una de las opciones: ")
    if opcion ==  "1":
        cant_10 = int(input("¿Cuantos billetes de 10 hay en la caja?: "))
    elif opcion == "2":
        cant_20 = int(input("¿Cuantos billetes de 20 hay en la caja?: "))
    elif opcion == "3":
        cant_50 = int(input("¿Cuantos billetes de 50 hay en la caja?: "))
    elif opcion == "4":
        cant_100 = int(input("¿Cuantos billetes de 100 hay en la caja?: "))
    elif opcion == "5":
        cant_200 = int(input("¿Cuantos billetes de 200 hay en la caja?: "))
    elif opcion == "6":
        cant_500 = int(input("¿Cuantos billetes de 500 hay en la caja?: "))
    elif opcion == "7":
        cant_1000 = int(input("¿Cuantos billetes de 1000 hay en la caja?: "))
    elif opcion == "8":
        print("Espero que te haya servido , nos vemos.")
        os.system('clear')
        return opcion 


menu()

def total():
    global total
    total = 10*cant_10+20*cant_20+50*cant_50+100*cant_100+200*cant_200+500*cant_500+1000*cant_1000
    
opcion=0

while opcion != "8":
    opcion = menu()