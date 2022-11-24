# Arqueo de Caja Speedruneado


print("Bienvenido al arqueador de caja - Designed by Gian Carlini")
print("Gusti pelotudooooooooooooooooooooooooooooooooooooooooooooo")
total_sistema = int(input("¿Cuanto dinero dice que hay en el sistema?"))

billetes_10 = 10 * int(input("¿Cuantos billetes de 10 tenes? "))

billetes_20 = 20 * int(input("¿Cuantos billetes de 20 tenes? "))

total_caja = billetes_10 + billetes_20


if total_caja == total_sistema:
    print("Nos podemos ir , la caja esta bien.")
    
elif total_caja != total_sistema:
    print("La caja no dio , hace las cosas bien o te mato")
    
