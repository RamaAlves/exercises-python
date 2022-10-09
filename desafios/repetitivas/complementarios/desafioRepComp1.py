""" Determinar el número mayor de 10 números ingresados. """

listaNumeros=[]

while len(listaNumeros)<10:
    numero=int(input("Ingrese un numero:\t"))
    listaNumeros.append(numero)

listaAux=[]

for numero in listaNumeros:
    listaAux.append(numero)
    if len(listaAux)==2:
        if listaAux[0]>=listaAux[1]:
            listaAux.pop(1)
        else:
            listaAux.pop(0)

print(listaAux[0])