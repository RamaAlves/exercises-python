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

print ("para operar entre diferentes tipos de ")
edad= 28
palabra_2= "Hola mundo"
suma = str(edad) + palabra_2

print(suma)

# operadores +, +=, -, -=, *, *=, //, /=, **, % 
# operadores logicos ==, <=, >=, <, >, and, or, ^(xor), not 

""" usos para xor
    xor es el operador or pero solo exclusivo es decir, solo da verdadero si una de las dos afirmaciones es correcta
    ademas el operador xor niega an nivel de bits
    por ejemplo si quiero intercambiar dos variables sin utilizar una variable auxiliar puedo valerme de Xor
    si hago a xor= b , me otorga la negacion de a y b y la almacena en a , luego b xor= a, que me otorga el valor que almacenaba a 
    ya que si opero la negacion de a y b con b me queda a y esta se almacena en b, por ultimo al volver a realizar
    a xor= b opero a que contiene la negacion de a y b con b que almacena en este momento el valor de a
    el resultado de esto da b. Por lo tanto se intercambian los valores de a y b  
 """

a= 5
b= 3
print(a,b)
a^=b 
b^=a 
a^=b
print(a,b)




#listas: se escriben entre corchetes. son un conjunto ordenado de elementos los mismos estan indizados

lista = [1,2,3,4,"auto",6]
print("la lista es: ", lista)
print(type(lista))
print(f"Mi lista tiene {len(lista)} cantidad de elementos")

#tupla: se escribe entre (). es similar a las tuplas pero esta es inmutable

tupla = (1,2,3,5,"flores",6)
print("la tupla es: ", tupla)
print(type(tupla))
print(f"Mi tupla tiene {len(tupla)} cantidad de elementos")

#set: es un conjunto desordenados de elementos. no se pueden repetir los valores 

set_ = {1,2,"rapido",5,80.5,2}
print(type(set_))

#diccionarios: son pares clave valor (lo mas parecido a un json)

diccionario = {1:"45", "b":20, "z":56.2}
print(type(diccionario))