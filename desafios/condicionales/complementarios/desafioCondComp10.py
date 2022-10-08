""" Tres personas deciden invertir su dinero para fundar una empresa. Cada una de ellas invierte una cantidad distinta. 
Obtener el porcentaje que cada quien invierte con respecto a la cantidad total invertida. """

ingreso1=float(input("Ingrese el monto que desea invertir:\t$ "))
ingreso2=float(input("Ingrese el monto que desea invertir:\t$ "))
ingreso3=float(input("Ingrese el monto que desea invertir:\t$ "))
totalInvertido=ingreso1+ingreso2+ingreso3

if totalInvertido>0:
    inversion1=(ingreso1/totalInvertido)*100
    inversion2=(ingreso2/totalInvertido)*100
    inversion3=(ingreso3/totalInvertido)*100
    print(f"La inversion total fue: $ {totalInvertido}")
    print(f"El primer inversor aportó $ {ingreso1} y su porcentaje es {inversion1}% del total")
    print(f"El segundo inversor aportó $ {ingreso2} y su porcentaje es {inversion2}% del total")
    print(f"El tercero inversor aportó $ {ingreso3} y su porcentaje es {inversion3}% del total")
else:
    print("Deben invertir dinero para hacer el calculo")