""" Solicite al usuario el ingreso de 3 números, e imprímalos de mayor a menor """

numero1=int(input("ingrese un numero:\t"))
numero2=int(input("ingrese un numero:\t"))
numero3=int(input("ingrese un numero:\t"))

if numero1>numero2 and numero1>numero3:
    if numero2>numero3:
        print(numero1,numero2,numero3)
    else:
        print(numero1,numero3,numero2)
elif numero2>numero1 and numero2>numero3:
    if numero1>numero3:
        print(numero2,numero1,numero3)
    else:
        print(numero2,numero3,numero1)
else:
    if numero1>numero2:
        print(numero3,numero1,numero2)
    else:
        print(numero3,numero2,numero1)