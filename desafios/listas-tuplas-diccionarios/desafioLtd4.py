""" Escribir un programa que cargue una tupla con nombres de especie, y para cada nombre de especie imprima el mensaje Hola soy ......, cuidame.
Modificá el programa anterior y dada una posición inicial p y una cantidad n, imprima el mensaje anterior para los n nombres que se encuentran a partir de la posición i. """

listaDeEspecies= ("Demonio de tazmania", "rata australiana", "correcaminos", "saltamontes hindu", "gato azul de las montañas", "perro marciano", "Gato violeta")

""" #solucion1
for especie in listaDeEspecies:
    print(f"hola soy {especie}, cuidame.")
 """
#solucion2
comienzaEn= int(input("ingrese la posicion donde desea comenzar a recorrer la tupla:\t"))-1
cantidadEspecies=int(input("indique la cantidad de posiciones que desea recorrer dentro de la tupla:\t"))

for i in range(cantidadEspecies):
    print(f"hola soy {listaDeEspecies[comienzaEn+i]}, cuidame.")
