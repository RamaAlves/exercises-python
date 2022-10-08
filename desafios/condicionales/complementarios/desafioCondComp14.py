""" Leer 2 números; si son iguales que los multiplique, si el primero es mayor que el segundo que los reste y si no que los sume. """

numero1=int(input("Ingrese un número:\t"))
numero2=int(input("Ingrese un número:\t"))

if numero1==numero2:
    total=numero1*numero2
    print("El resultado es:\t",total)
elif numero1>numero2:
    total=numero1-numero2
    print("El resultado es:\t",total)
else:
    total=numero1+numero2
    print("El resultado es:\t",total)