""" Determinar si un alumno aprueba a reprueba un curso, 
sabiendo que aprobara si su promedio de tres calificaciones es mayor o igual a 70; desaprueba en caso contrario. """

nota1=int(input("ingrese la calificacion:\t"))
nota2=int(input("ingrese la calificacion:\t"))
nota3=int(input("ingrese la calificacion:\t"))

promedio=(nota1+nota2+nota3)/3

if promedio==100:
    print("Aprobado. Sobresaliente\nSu promedio es de: ", promedio)
elif promedio>=90:
    print("Aprobado. Casi sobresaliente\nSu promedio es de: ", promedio)
elif promedio>=80:
    print("Aprobado. Muy Bien\nSu promedio es de: ", promedio)
elif promedio>=70:
    print("Aprobado. Bien\nSu promedio es de: ", promedio)
elif promedio<=60:
    print("Aprobado.\nSu promedio es de: ", promedio)
else:
    print("Desaprobado")