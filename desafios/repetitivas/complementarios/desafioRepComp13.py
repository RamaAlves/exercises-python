""" Un grupo de 100 estudiantes presentan un exámen de Física. Diseñe un diagrama que lea por cada estudiante la calificación obtenida y calcule e imprima:
A.- La cantidad de estudiantes que obtuvieron una calificación menor a 50.
B.- La cantidad de estudiantes que obtuvieron una calificación de 50 o más pero menor que 80.
C.- La cantidad de estudiantes que obtuvieron una calificación de 70 o más pero menor que 80.
D.- La cantidad de estudiantes que obtuvieron una calificación de 80 o más. """

import random

contador=0
listaCalificaciones=[]
menos50=0
menos80=0
entre70Y80=0
mas80=0

while contador<100:
    contador+=1
    calificacion=(random.randint(1,100))
    listaCalificaciones.append(calificacion)

for calificacion in listaCalificaciones:
    if calificacion<50:
        menos50+=1
    elif calificacion<80:
        menos80+=1
        if calificacion>=70:
            entre70Y80+=1
    else:
        mas80+=1

print("De un total de 100 estudiantes que presentaron el examen de Fisica:")
print(menos50," obtubieron una calificación menor a 50 pts")
print(menos80," obtubieron una calificación entre 50 pts y 79 pts")
print("De estos últimos ",entre70Y80," obtubieron una calificación entre 70 pts y 79 pts")
print("por último ",mas80," obtubieron una calificación de 80 pts o más")