# operadores +, +=, -, -=, *, *=, //, /=, **, % 

#suma
sumando_1=85
sumando_2=69
suma= sumando_1+sumando_2
print(f"La suma de {sumando_1} y {sumando_2} es:\n {suma}")

#resta
minuendo= 52
sustraendo= 66
diferencia= minuendo-sustraendo
print(f"La resta de {minuendo}-{sustraendo} es:\n {diferencia}")

#multiplicacion
multiplicando= 40
multiplicador= 3
producto= multiplicando*multiplicador
print ("El resultado de la multiplicacion entre ", multiplicando," y ", multiplicador, " es:\n ", producto)

#division
dividendo= 21
divisor=4
cociente= dividendo/divisor
print( "el resultado de la division de "+str(dividendo)+" por "+str(divisor)+" es:\n "+str(cociente))

#division entera
dividendo_entero= 24
divisor_entero= 5
cociente_entero= dividendo_entero//divisor_entero
resultado= "El resultado de la división entera de {} por {} es:\n {}".format(dividendo_entero, divisor_entero, cociente_entero,)
print(resultado)

#modulo (resto)
dividendo_resto=21
divisor_resto=3
resto= 21%3
print(f"El resto de la division de {dividendo_resto} dividido {divisor_resto} es:\n {resto}")

#potencia
base= 8
exponente= 2
potencia= base**exponente
print(f"El resultado de la potencia de {base} elevado al {exponente} es:\n {potencia}")


# operadores logicos ==, <=, >=, <, >, and, or, ^(xor), not 
print("operadores lógicos")

verdadero= True
falso= False 

#AND
comparacion= verdadero and verdadero
print("si x1 and x2 and xn... son verdaderos: ", comparacion)

#OR 
si_al_menos_uno= verdadero or falso
print (f"si al menos un termino es verdadero: \n verdadero or falso --> {si_al_menos_uno}")

#NOT
opuesto= not verdadero
print(f"el operador not devuelve el valor opuesto, por ejemplo:\n not {verdadero} --> {opuesto}")

""" usos para xor
    xor es el operador or pero solo exclusivo es decir, solo da verdadero si una de las dos afirmaciones es correcta
    ademas el operador xor niega an nivel de bits(^)
    por ejemplo si quiero intercambiar dos variables sin utilizar una variable auxiliar puedo valerme de Xor
    si hago a xor= b , me otorga la negacion de a y b y la almacena en a , luego b xor= a, que me otorga el valor que almacenaba a 
    ya que si opero la negacion de a y b con b me queda a y esta se almacena en b, por ultimo al volver a realizar
    a xor= b opero a que contiene la negacion de a y b con b que almacena en este momento el valor de a
    el resultado de esto da b. Por lo tanto se intercambian los valores de a y b 
    para usar xor debo definirlo ya que no es nativo en python 
 """
#xor 
def xor(n_1, n_2):
    xor=False
    xor= (n_1 or n_2) and not (n_1 and n_2)
    return xor

o_exclusivo= xor(verdadero, falso)
print (f"el o exclusivo solo devuelve verdadero si una sola de sus partes es verdadera: \n verdadero xor falso or falso xor verdadero -->{o_exclusivo}") 

#xor bit a bit
print("xor bit a bit ^")

a= 5
b= 3
print(a,b)
a^=b 
b^=a 
a^=b
print(a,b)
#>
print("> solo da verdadero cuando el valor a su izquierda es mayor que el de la derecha")
print("3 > 2", (3>2),"\n4 > 5", (4>5))

#<
print("< solo da verdadero cuando el valor a su izquierda es menor que el de la derecha")
print("1 < 2", (1<2),"\n7 < 5", (7<5))

#==
print("== otorga verdadero si los valores a ambos lados del operador son iguales")
print("4==4", (4==4), "\n4==3", (4==3))

#>=
print(">= otorga verdadero cuando el valor a su izquierda es mayor o igual al de su derecha")
print("4>=3", (4>=3),"\n4>=4", (4>=4),"\n4>=5",(4>=5))

#<=
print("<= otorga verdadero cuando el valor a su izquierda es menor o igual al de su derecha")
print("3<=4", (3<=4),"\n4<=4", (4<=4),"\n4<=5",(5<=4))

#!=
print("!= otorga verdadero cuando los valores a sus lados son diferentes")
print("4!=3", (4!=3),"\n4!=4",(4!=4),"\n4!=5",(4!=5))