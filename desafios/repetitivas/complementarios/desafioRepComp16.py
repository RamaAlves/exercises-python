""" Escribir un programa el cual lea dos valores enteros. Si el primero es menor que el segundo, que imprima el mensaje ``Arriba''. 
Si el segundo es menor que el primero, que imprima el mensaje ``Abajo''. Si los números son iguales, que imprima el mensaje ``igual''. 
Si alguno de los datos ingresados es igual a 0, que imprima un mensaje conteniendo la palabra ``Error''. """

for i in range(5):
    numero1=int(input("Ingrese un numero:\t"))
    numero2=int(input("Ingrese otro numero:\t"))
    if numero1==0 or numero2==0:
        print("''Error''")
    elif numero1==numero2:
        print("''Igual''")
    elif numero1<numero2:
        print("''Arriba''")
    else:
        print("Abajo")
