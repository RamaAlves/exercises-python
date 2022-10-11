""" Imprimir, contar y sumar los múltiplos de 2 que hay entre una serie de números, tal que el segundo sea mayor o igual que el primero. """

import random

print("Jugando con los multiplos de 2.")
print("Se generará una lista de numeros de manera automatica")
print("Se imprimirán, contarán y sumarán todos los multiplos de 2. Los numeros se ordenarán de menor a mayor\t")

contadorPares=0
acumuladorPares=0
listaNumerosAutomatica=[]
listaPares=[]

longitudLista=int(input("Ingrese la cantidad de numeros aleatorios que desea agregar a la lista para comenzar a jugar:    "))
print("Procesando...")
for numero in range(longitudLista):
    listaNumerosAutomatica.append(random.randint(1,100))

print("La lista de numeros generada es:", listaNumerosAutomatica)
print("Se ordenaran los numeros de menor a mayor para operar con ellos")
print("Procesando...")
listaNumerosAutomaticaOrdenada= sorted(listaNumerosAutomatica)

for numero in listaNumerosAutomaticaOrdenada:
    if numero%2 ==0:
        listaPares.append(numero)
        contadorPares+=1
        acumuladorPares+=numero

if len(listaPares)>=1:
    print("Los numeros pares (ordenados de menor a mayor) en la lista son:")
    for numero in listaPares:
        print(numero, end=", ")
    print(f"\nEntre {listaNumerosAutomatica} hubo un total de: {contadorPares} numeros pares.\nLa suma de todos los números pares es: {acumuladorPares}")
else:
    print("No hay numeros pares en la lista generada")