""" Para el uso de fertilizantes es necesario medir cuánto abarca un determinado compuesto en el suelo el cual debe existir en una cantidad 
de al menos 10% por hectárea, y no debe existir vegetación del tipo MATORRAL. Escribir un programa que determine si es factible la utilización de fertilizantes. """

hectareas=float(input("Ingrese tamaño en hectareas"))
compuesto=float(input("nivel de compuesto en el suelo"))
matorral=input("hay vegetacion de tipo matorral? (y/n) ").lower()

porcentaje = compuesto*100/hectareas

if porcentaje >=10 and matorral == "n":
    print("se puede usar fertilizantes!")
else:
    print("no se puede usar fertilizantes")
