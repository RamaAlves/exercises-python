""" Un obrero necesita calcular su salario semanal, el cual se obtiene de la siguiente manera:
i. Si trabaja 40 horas o menos se le paga $16 por hora
ii. Si trabaja más de 40 horas se le paga $16 por cada una de las primeras 40 horas y $20 por cada hora extra. """

horas=int(input("Ingrese la cantidad de horas trabajadas en la semana:\t"))

if horas>40:
    sueldo=40*16+(horas-40)*20
    print("Su sueldo es:\t$", sueldo)
else:
    sueldo=horas*16
    print("Su sueldo es:\t$", sueldo)