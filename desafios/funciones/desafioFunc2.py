""" Realiza una función llamada relacion(a, b) que a partir de toneladas recicladas de dos ciudades se cumpla lo siguiente:
Si el primer número es mayor que el segundo, debe devolver el nombre de la ciudad 1.
Si el primer número es menor que el segundo, debe devolver el nombre de la ciudad 2.
Si ambos números son iguales, debe devolver el nombre de ambas.
 """
reciclajeSaltadillaEnTn=int(input("Indique la cantidad de toneladas recicladas por la de Saltadilla:\n"))
reciclajeGothamEnTn=int(input("Indique la cantidad de toneladas recicladas por la de Gotham City:\n"))

def relacion(a,b):
    if a == b:
        print("Saltadilla y Gotham City")
    elif a>b:
        print("Saltadilla")
    else:
        print("Gotham City")

relacion(reciclajeSaltadillaEnTn, reciclajeGothamEnTn)
