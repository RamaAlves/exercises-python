""" Realiza una función separar(lista) que tome una lista que tenga datos de cantidad de árboles plantados en diferentes ciudades de Argentina
durante la cuarentena. Luego la función debe devolver dos listas ordenadas. La primera con las cantidades que superen los 100 y la segunda con el resto.
Qué cantidad de ciudades han plantado más de 100 árboles durante cuarentena. """

cantidadDeArbolesPorCiudad= [200,44,52,89,500,61,382,46,300,12]
ciudadesConMasDe100=[]
ciudadesConMenosDe100=[]

def separar(lista):
    for elemento in lista:
        if elemento>100:
            ciudadesConMasDe100.append(elemento)
        else:
            ciudadesConMenosDe100.append(elemento)


separar(cantidadDeArbolesPorCiudad)

ciudadesConMasDe100.sort()
ciudadesConMenosDe100.sort()
print(ciudadesConMasDe100)
print(ciudadesConMenosDe100)