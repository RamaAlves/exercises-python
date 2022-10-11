""" Mostrar los perímetros de varios triángulos ingresados sus lados por teclado, hasta que ya no desee """
continuar=bool(1)

while continuar:
    lado1=float(input("Ingrese el lado 1:\t"))
    lado2=float(input("Ingrese el lado 2:\t"))
    lado3=float(input("Ingrese el lado 3:\t"))
    print(f"El perimetro es: {lado1+lado2+lado3}")
    continuar=bool(int(input("Desea continuar ingresando triangulos?\n(Presione 0 para finalizar)\n")))

print("Adios!")