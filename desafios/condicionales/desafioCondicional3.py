""" Para el uso de fertilizantes es necesario medir cuánto abarca un determinado compuesto en el suelo el cual debe existir en una cantidad 
de al menos 10% por hectárea, y no debe existir vegetación del tipo MATORRAL. Escribir un programa que determine si es factible la utilización de fertilizantes. """

compuesto_en_suelo=input("existe al menos un 10% de compuesto x por hectárea? (y/n) ").lower()
matorral=input("hay vegetacion de tipo matorral? (y/n) ").lower()

if compuesto_en_suelo =="y" and matorral == "n":
    print("se puede usar fertilizantes!")
else:
    print("no se puede usar fertilizantes")
