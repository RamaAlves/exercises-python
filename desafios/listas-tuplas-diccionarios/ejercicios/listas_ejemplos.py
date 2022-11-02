""" tipo de dato que permite manejar grandes cantidades de elementos y trabajar con ellos. Se puede modificar los mismos"""
lista_vacia= []
print(f"esto es una lista vacia {lista_vacia}")
print(f"la variable lista vacia es de tipo {type(lista_vacia)}")

nueva_lista= list()
print(f"esto es una nueva lista {nueva_lista}")
print(f"la variable nueva lista es de tipo {type(nueva_lista)}")

""" ejemplos """

#lista de frutas
frutas= ["naranja","banana","anana"]
#lista de numeros
numeros=[1,2,6,5]
print(f"lista de frutas{frutas}")
print(f"lista de numeros{numeros}")

#lista mezclada

mezcla=[1,2.5,"hola"]
print(f"esta lista tiene datos mezclados: {mezcla}")

""" las listas tienen un indice:

['auto', 'casa', 'perro', 5 ]
    0       1       2     3

"""

lista_indices=['auto', 'casa', 'perro',5]

una_cosa=lista_indices[0]
print(f"lista: {lista_indices}")
print(f"en la posicion 0 se encuentra{una_cosa}")

#puedo acceder desde el final con indices negativos
ultima_cosa=lista_indices[-1]
print(f"Ultimo elemento {ultima_cosa}")

#se puede modicar directamente un elemento pasando el indice y reescribiendolo
print(lista_indices)
lista_indices[0]="carro"
print("lista con primer elemento modificados",lista_indices)

#ver una seccion de la lista
sub_lista=lista_indices[0:3]#primeros 3 elementos
print(sub_lista)
print(f"primeros 3 elementos de lista_indices: {sub_lista}")
sub_lista=lista_indices[:2]#primeros 2 elementos
print(sub_lista)
print(f"primeros 2 elementos de lista_indices: {sub_lista}")
sub_lista=lista_indices[2:]#ultimos 2 elementos
print(f"ultimos 2 elementos de lista_indices: {sub_lista}")

#copia lista_indices
copia_lista_indices=lista_indices[:]
print(f"copia de lista_indices:{copia_lista_indices}")

#sub lista con saltos
sub_lista_saltos=lista_indices[0:3:2]
print("lista original: ",lista_indices)
print(f"lista con saltos: {sub_lista_saltos}")

""" para recorrer una lista se puede utilizar la estructura for """

for elemento in lista_indices:
    print(f"elemento:\t{elemento}")
    
""" si quiero mostrar los indices se usa enumerate(iterable) y agrega una variable local en el for(el primer elemento es el contador) """

verduras=["papa", "cebolla", "rucula"]

for contador, una_verdura in enumerate(verduras):
    print(f"En la posicion {contador} esta una {una_verdura}")

""" para iterar por mas de una lista puedo usar zip """

famosos=["Tom Cruise", "Jhonny Deep", "arturo", "lautaro"]
edades=[44,85,45,80]

for famoso, edad in zip(famosos, edades):
    print(f"{famoso} tiene {edad} años de edad")

#lista con saltos
for famoso, edad in zip(famosos[::2], edades[::2]):
    print(f"{famoso} tiene {edad} años de edad")

""" se puede averiguar si un elemento esta o no en una lista puede usar "in" o "not in" (devuelve un bool) """

print("Tom Cruise" in famosos)
print("Tom Cruis" in famosos)

print("Jhonny Deep" not in famosos)
print("Jhonny Dep" not in famosos)

""" agregar elementos nuevos a la lista """

colores= ["rojo","azul"]
print (colores)
colores.append("amarillo")
print (colores)
#agregar una lista a la lista
colores_secundarios=["naranja", "violeta", "verde"]
colores.append(colores_secundarios)
print(colores)
#si uso extend() los elementos de la nueva lista se concatenan
colores=["rojo","azul","amarillo"]
print(colores)
colores.extend(colores_secundarios)
print(colores)

#otra forma
colores=["rojo","azul","amarillo"]
colores_extendidos= colores+colores_secundarios
print(colores_extendidos)
""" agregar elementos  con insert() """

colores_extendidos.insert(2, "magenta")
print(colores_extendidos)

#con remove elimino elementos por valores pasados por parametro

colores_extendidos.remove("magenta")
print(colores_extendidos)

#en cambio si quiero eliminar un elemento por su indice
del colores_extendidos[4]
print(colores_extendidos)

#pop() elimina el ultimo elemento o segun la posicion pasada como parametro

print(colores_extendidos)
color_eliminado=colores_extendidos.pop()
print(colores_extendidos)
print(color_eliminado)
color_eliminado=colores_extendidos.pop(2)
print(colores_extendidos)
print(color_eliminado)

#count(parametro) sirve para saber cuantas veces aparece el parametro en mi lista
numeros_x= [1,2,3,1,2,2,1,3,2]
numero_1=numeros_x.count(1)
print(numeros_x)
print(f"cantidad de numeros 1: {numero_1}")

#reverse
sys=["windows","linux", "mac"]

print(sys)
sys.reverse()
sys_reverse= sys
print(sys_reverse)
sys_restore=sys[::-1]
print(sys_restore)

#copiar una lista para que no se modifiquen
#metodo copy

#sort() Ordenar
numeros=[2,5,9,51,3,8,6]
print(numeros)
numeros.sort()
print(f"lista ordenada {numeros}")
numeros.sort(reverse=True)
print(numeros)

#index
print(numeros)
indice=numeros.index(5)
print(indice)

#max
maximo=max(numeros)

#min
minimo=min(numeros)

print("maximo: ",maximo, "minimo", minimo)

