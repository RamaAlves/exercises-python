""" Diseñar un programa que permita obtener el producto entre A y B mediante sumas sucesivas """

numero1=int(input("Ingrese el multiplicando:\t"))
numero2=int(input("Ingrese el multiplicador:\t"))
sumaAcumulada=0

for numero in range(numero2):
    sumaAcumulada+=numero1

print(sumaAcumulada)