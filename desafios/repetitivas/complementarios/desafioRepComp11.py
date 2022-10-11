""" Hacer un programa que permita determinar todos los divisores de un número ingresado por el teclado. """

numero=int(input("Ingrese un numero:\t"))
divisor=numero

print(f"Los divisores de {numero} son:")
while divisor >0:
    if numero%divisor==0:
        print(divisor)
    divisor-=1