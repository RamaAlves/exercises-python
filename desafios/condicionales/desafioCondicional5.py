""" La ciudad esta dividida en 2 secciones de recolección sección A y B de acuerdo al nombre de la barrio y el tipo del barrio (CÉNTRICO y NO CÉNTRICO)
La sección A esta formada por los barrios céntricos cuyo nombre comienza con una letra anterior a M y los barrios no céntricos con nombre posterior a la M, y la sección B el resto.
Debemos hacer un programa que dado el nombre del barrio y la ubicación, nos informe en que sección se encuentra. """

barrio= input("ingrese el nombre de su barrio:\n").capitalize()
es_centro= input("El barrio es centrico? (y/n):\n").lower()

if barrio<"M" and es_centro=="y" or barrio>"M" and es_centro=="n":
    print("Sección A")
else:
    print("Seccion B")