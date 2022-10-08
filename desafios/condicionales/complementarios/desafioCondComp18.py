""" Se leen tres números que son las longitudes de los lados de un triángulo. 
Determinar e informar si el mismo es equilátero (3 lados iguales), isósceles (2 lados iguales) o escaleno (3 lados distintos). """

print("Analicemos el triángulo:\n")
lado1=float(input("Ingrese un lado:\t"))
lado2=float(input("Ingrese el segundo lado:\t"))
lado3=float(input("Ingrese el último lado:\t"))

if lado1==lado2 and lado1==lado3:
    print("El triángulo es equilátero")
else:
    if lado1==lado2 or lado1==lado3 or lado2==lado3:
        print("El triángulo es isósceles")
    else:
        print("El triángulo es escaleno")