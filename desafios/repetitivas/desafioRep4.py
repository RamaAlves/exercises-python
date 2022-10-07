""" Escriba un programa que permita imprimir un tablero Ecológico (verde y blanco) de acuerdo al tamaño indicado. 
Por ejemplo el gráfico a la izquierda es el resultado de un tamaño: 8x6 """

print("creando un tablero ecologico")
alto=int(input("indique el alto (filas) del tablero (expresado en números):\t"))
ancho=int(input("indique el ancho (columnas) del tablero (expresado en números):\t"))
contadorFilas=0
verde=True
while contadorFilas<alto:
    contadorFilas+=1
    contadorCelda=0
    while contadorCelda<ancho:
        contadorCelda+=1
        if verde:
            print(" V ", end="")
            verde = not verde
        else:
            print(" B ", end="")
            verde = not verde
    print("")
    verde= not verde


""" alto=4
ancho=6
contadorFilas=0
verde=True
tablero=[]
while contadorFilas<alto:
    contadorFilas+=1
    contadorCelda=0
    fila=[]
    while contadorCelda<ancho:
        contadorCelda+=1
        if verde:
            fila.append("verde")
            print("verde")
            verde = not verde
        else:
            fila.append("blanco")
            print("blanco")
            verde = not verde
    tablero.append(fila)
    verde= not verde
print(tablero) """