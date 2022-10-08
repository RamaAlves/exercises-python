""" Diseñar un programa que lea las longitudes de los tres lados de un triángulo (L1,L2,L3) y determine qué tipo de triángulo es,
 de acuerdo a los siguientes casos. Suponiendo que A determina el mayor de los tres lados y B y C corresponden con los otros dos, entonces:
Si A>=B + C à No se trata de un triángulo
Si A^2 = B^2 + C^2 à Es un triángulo rectángulo
Si A^2 > B^2 + C^2 à Es un triángulo obtusángulo
Si A^2 < B^2 + C^2 à Es un triángulo acutángulo """

lado1=float(input("ingrese el lado mayor del triangulo"))
lado2=float(input("ingrese otro lado del triangulo"))
lado3=float(input("ingrese ingrese el lado restante del triangulo"))

triangulo=[lado1,lado2,lado3]
if triangulo[0]<(triangulo[1]+triangulo[2]):
    if (triangulo[0]**2)==((triangulo[1]**2)+(triangulo[2]**2)):
        print("el triangulo es rectángulo")
    elif (triangulo[0]**2)>((triangulo[1]**2)+(triangulo[2]**2)):
        print("el triangulo es obtusangulo")
    elif (triangulo[0]**2)<((triangulo[1]**2)+(triangulo[2]**2)):
        print("el triangulo es acutangulo")
    else:
        print("no es un triangulo")
else:
    print("no es un triangulo")