""" Hacer un programa que calcule el total a pagar por la compra de camisas. 
Si se compran tres camisas o mas se aplica un descuento del 20% sobre el total de la compra y si son menos de tres camisas un descuento del 10%. """

camisa=2000
print(f"Cada camisa cuesta:\t${camisa}")
cantidad=int(input("cuantas camisas compra?\n(Ingrese un numero)\n\n\t"))

if cantidad>=3:
    totalSinDescuento=camisa*cantidad
    totalConDescuento=totalSinDescuento*0.8
    print(f"Su total sin descuento es de:\t${totalSinDescuento}\nSu descuento es de un 20%\nSu total a pagar con descuento es de:\t${totalConDescuento}")
elif cantidad<3 and cantidad>0:
    totalSinDescuento=camisa*cantidad
    totalConDescuento=totalSinDescuento*0.9
    print(f"Su total sin descuento es de:\t${totalSinDescuento}\nSu descuento es de un 10%\nSu total a pagar con descuento es de:\t${totalConDescuento}")
else:
    print("debe comprar al menos una camisa")