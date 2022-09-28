# Variables son elementos que permiten guardar un dato para manipularlo y transformarlo
#Numeros enteros

numero_entero=24
print(f"El numero es: {numero_entero}")
print(f"El tipo de dato es: {type(numero_entero)}")

#Numeros reales
numero_real=20.56
print(f"El numero es: {numero_real}")
print("El tipo de dato es: "+str({type(numero_real)}))

#Numeros complejos
complejo=16 +6j
print(f"El numero es: {complejo}")
print(f"El tipo de dato es: {type(complejo)}")

#Booleano
booleano=True
print(f"El booleano es: {booleano}")
print(f"El tipo de dato es: {type(booleano)}")

#String
string="Estoy programando"
print("El texto es: {}".format(string))
print("El tipo de dato es:", {type(string)})

#None
none=None
print("La variable es: {}".format(none))
print(f"El tipo de dato es: {type(none)}")

#cambiando tipos

palabra = "hola informatorio"

print("mi variable palabra contiene: ",palabra)
print(type(palabra))

# cambiar tipo de variable (tipado dinamico)

palabra = 23.3
print ("cambiar tipo.")
print("mi variable palabra ahora contiene: ", palabra)
print(type(palabra))

# debido a que es fuertemente tipado (no confundir con tipado dinamico) no se pueda operar con diferentes tipos de variables

# suma= edad+palabra_2
# error
# print(suma)

""" 
para solucionar este error debo cambiar el tipo de dato de alguna de las 2 variables
puedo utilizar: int(), str(), float(), bool() ..."""

print ("para operar entre diferentes tipos de datos primero debo transformar todos los datos al mismo tipo")
edad= 28
palabra_2= "Hola mundo"
suma = str(edad) + palabra_2

print(suma)


#listas: se escriben entre corchetes. son un conjunto ordenado de elementos los mismos estan indizados. se puede modificar

lista = [1,2,3,4,"auto",6]
print("La lista contiene: ", lista)
print(type(lista))
print(f"Mi lista tiene {len(lista)} cantidad de elementos")
lista[3]="perro"
print(f"La lista contiene: {lista}")

#tupla: se escribe entre (). es similar a las listas pero esta es inmutable

tupla = (1,2,3,5,"flores",6)
print("la tupla es: ", tupla)
print(type(tupla))
print(f"Mi tupla tiene {len(tupla)} cantidad de elementos")

#set: es un conjunto desordenados de elementos. no se pueden repetir los elementos

set_ = {1,2,"rapido",5,80.5,2}
print(set_)
print(type(set_))

#frozenset: es similar al set salvo que no se puede modificar, solo al inicializar

fs=frozenset([1,2,3])
print(fs)
print(type(fs))

#diccionarios: son pares clave valor (lo mas parecido a un json)

diccionario = {1:"45", "b":20, "z":56.2}
print(type(diccionario))
print(f"dentro del diccionario con la clave 1 tengo el valor: {diccionario[1]}")


#concatenacion de strings

string_1 = "Hola "
string_2 = "informatorio!"
concatenacion= string_1+string_2
print(f"concatenacion de strings: '{string_1}'+'{string_2}' \n {concatenacion}")

#multiplicacion de strings

eco= "eco... "*3
print ("multiplicacion de strings:\n", eco)

#mezcla

mezcla= eco + string_1 + "mundirijillo"
print(f"Mezcla de strings: \n{mezcla}")