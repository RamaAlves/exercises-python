""" En un supermercado se hace una promoción, mediante la cual el cliente obtiene un descuento dependiendo de un número que se escoge al azar. 
Si el numero escogido es menor que 74 el descuento es del 15% sobre el total de la compra, 
si es mayor o igual a 74 el descuento es del 20%. Obtener cuánto dinero se le descuenta. """

import random

importe=float(input("Ingrese el total de la compra:\t$"))

if random.randint(1,100)>=74:
    descuento=importe*0.20
    total=importe-descuento
    print("su descuento es del 20%")
    print ("seran descontados:\t$", descuento)
    print ("el total a pagar es:\t$",total)
else:
    descuento=importe*0.15
    total=importe-descuento
    print("Su descuento es del 15%")
    print ("seran descontados:\t$", descuento)
    print ("el total a pagar es:\t$",total)