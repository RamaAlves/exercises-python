""" Un equipo de fútbol ha tenido una buena campaña y desea premiar a sus jugadores con un aumento del salario para la siguiente campaña. 
Los sueldos deben ajustarse de la siguiente forma:
Sueldo Actual (en $)    Aumento
0 – 6000				15%
6000 – 7900			    10%
7900 – 12000			6%
Más de 12000		    0%
Diseñar un programa que lea el salario de un jugador, y que a continuación muestre el tanto por ciento de aumento, el sueldo actual y el sueldo aumentado. """

sueldo=float(input("Ingrese su sueldo:\t"))

if sueldo<=6000:
    aumento= sueldo*1.15
    print(f"Le corresponde un aumento del 15%, su sueldo actual es: ${sueldo}. Su sueldo con aumento será: ${aumento}")
elif sueldo>6000 and sueldo<=7900:
    aumento= sueldo*1.10
    print(f"Le corresponde un aumento del 10%, su sueldo actual es: ${sueldo}. Su sueldo con aumento será: ${aumento}")
elif sueldo>7900 and sueldo<=12000:
    aumento= sueldo*1.06
    print(f"Le corresponde un aumento del 6%, su sueldo actual es: ${sueldo}. Su sueldo con aumento será: ${aumento}")
else:
    aumento= sueldo
    print(f"No le corresponde aumento, su sueldo actual es: ${sueldo}.")