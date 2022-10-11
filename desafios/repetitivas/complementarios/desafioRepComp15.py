""" En un supermercado se hace una promoción, mediante la cual el cliente obtiene un descuento dependiendo de un número que se escoge al azar. 
Si el número escogido es menor que 50 el descuento es del 15% sobre el total de la compra, 
si es mayor o igual a 50 el descuento es del 20%. Obtener cuánto dinero se le descuenta. """

import random

sortear=True
while sortear:
    numero=random.randint(1,99)
    precio=float(input("Ingrese el monto de la compra: $"))
    if numero<50:
        total=precio*0.85
        print("Su descuento es de un 15%")
        print("Debe pagar: $",total)
    else:
        total=precio*0.80
        print("Su descuento es de un 20%")
        print("Debe pagar: $",total)
    continuar=int(input("Desea cargar mas productos?\n(Presione 1 para continuar o 0 para finalizar)\n"))
    if not bool(continuar):
        sortear=False
print("Adios!")