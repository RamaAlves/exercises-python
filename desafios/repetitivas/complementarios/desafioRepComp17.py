""" Calcular la utilidad que un trabajador recibe en el reparto anual de utilidades si este se le asigna como un porcentaje de su salario mensual 
que depende de su antigüedad en la empresa de acuerdo con la sig. tabla:

Tiempo												Utilidad
Menos de 1 año								        5% del salario
Más de 1 año y hasta 2 años		                    7% del salario
Más de 2 años y hasta 5 años                        10% del salario
Más de 5 años y hasta 10 años                        15% del salario
Más de 10 años								        20% del salario """

trabajadores=int(input("Indique la utilidad de cuantos trabajadores quiere calcular:\t"))

for trabajador in range(trabajadores):
    antiguedad=int(input(f"Ingrese la cantidad de años de antiguedad que tiene el trabajador {trabajador+1} en la empresa:\t"))
    salario=int(input("ingrese el salario actual:\t"))
    if antiguedad ==0:
        utilidad=salario*0.05
        print(f"Le corresponde un 5% de su salario como utilidad. ${utilidad}")
    elif antiguedad>0 and antiguedad<=2:
        utilidad=salario*0.07
        print(f"Le corresponde un 7% de su salario como utilidad. ${utilidad}")
    elif antiguedad>2 and antiguedad<=5:
        utilidad=salario*0.1
        print(f"Le corresponde un 10% de su salario como utilidad. ${utilidad}")
    elif antiguedad>5 and antiguedad<=10:
        utilidad=salario*0.15
        print(f"Le corresponde un 15% de su salario como utilidad. ${utilidad}")
    else:
        utilidad=salario*0.2
        print(f"Le corresponde un 20% de su salario como utilidad. ${utilidad}")