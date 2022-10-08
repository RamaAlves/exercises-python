""" Realizar un programa que sea capaz de, habiéndose ingresado dos números m y n, determine si n es divisor de m. """

numero1=float(input("ingrese un numero:\t"))
numero2=float(input("ingrese un numero:\t"))

if (numero1%numero2)==0:
    print(f"{numero2} es divisor de {numero1}")
else:
    print(f"{numero2} no es divisor de {numero1}")