""" Determinar si el primero de un conjunto de tres números dados, es menor que los otros dos. """

numero1=input("ingrese un numero:\t")
numero2=input("ingrese un numero:\t")
numero3=input("ingrese un numero:\t")
conjunto={numero1,numero2,numero3}
lista=[]

for numero in conjunto:
    lista.append(numero)

if lista[0]<lista[1] and lista[0]<lista[2]:
    print("El primero es menor")
    print(lista)
else:
    print("El primero no es menor")
    print(lista)