""" Realiza una función separar(lista) que tome una lista que tenga datos de cantidad de árboles plantados en diferentes ciudades de Argentina
durante la cuarentena. Luego la función debe devolver dos listas ordenadas. La primera con las cantidades que superen los 100 y la segunda con el resto.
Qué cantidad de ciudades han plantado más de 100 árboles durante cuarentena. """

""" arbolesPlantados= [200,44,52,89,500,61,382,46,300,12]
ciudadesConMasDe100=[]
ciudadesConMenosDe100=[]

def separar(lista):
    for elemento in lista:
        if elemento>100:
            ciudadesConMasDe100.append(elemento)
        else:
            ciudadesConMenosDe100.append(elemento)


separar(arbolesPlantados)

ciudadesConMasDe100.sort()
ciudadesConMenosDe100.sort()
print(ciudadesConMasDe100)
print(ciudadesConMenosDe100)
 """
#modificacion para recibir una lista de arboles plantados y las ciudades donde fueron plantadas
arbolesPlantados= [["Corrientes", 200],["Tintina", 80],["La Plata", 150],["Posadas", 95],["Cordoba", 400],["Resistencia", 30],["Saenz Peña", 113]]
ciudadesConMasDe100=[]
ciudadesConMenosDe100=[]

def separar(lista):
    for elemento in lista:
        if elemento[1]>100:
            ciudadesConMasDe100.append(elemento)
        else:
            ciudadesConMenosDe100.append(elemento)

separar(arbolesPlantados)

ciudadesConMasDe100.sort(key=lambda elemento: elemento[1])
ciudadesConMenosDe100.sort(key=lambda elemento: elemento[1])

for ciudad in ciudadesConMasDe100:
    print(f"{ciudad[0]}: {ciudad[1]} arboles plantados")
for ciudad in ciudadesConMenosDe100:
    print(f"{ciudad[0]}: {ciudad[1]} arboles plantados")
