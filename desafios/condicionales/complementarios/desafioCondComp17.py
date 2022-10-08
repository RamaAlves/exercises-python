""" Determinar y exhibir si la estatura de una persona adulta dada, es mayor que la estatura media de las personas adultas de su sexo, siendo:

- estatura media de mujeres adultas: 1,65 m.
- estatura media de varones adultos: 1,72 m. """

estaturaMediaMujeres=1.65
estaturaMediaVarones=1.72

print("Controlemos su altura:\n\n")

sexo=input("Indique su sexo con:\n'm' para mujer\n'v' para varon\n").lower()

if sexo=='m':
    estatura=float(input("Ingrese su altura en metros:\n(ejemplo: 1.65)\n\n\t"))
    if estatura>estaturaMediaMujeres:
        print("Su altura está por encima de la media")
    elif estatura==estaturaMediaMujeres:
        print("Su estatura es igual a la media")
    else:
        print("su estatura está por debajo de la media")
elif sexo == "v":
    estatura=float(input("Ingrese su altura en metros:\n(ejemplo: 1.72)\n\n\t"))
    if estatura>estaturaMediaVarones:
        print("Su altura está por encima de la media")
    elif estatura==estaturaMediaVarones:
        print("Su estatura es igual a la media")
    else:
        print("su estatura está por debajo de la media")
else:
    print("El sexo indicado no se encuentra en nuestra base de datos")