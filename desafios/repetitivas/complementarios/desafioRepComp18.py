""" Diseña un programa al que se proporcione como entradas dos enteros y un carácter. El programa deberá sumar, restar, 
multiplicar o dividir los valores de los dos primeros parámetros dependiendo del código indicado en el tercer parámetro,
 y devolver el resultado. Por ejemplo si el usuario ingresa la opción “S”, se deberán sumar los números. """

print("Ingrese un codigo que contenga 2 numeros y una letra:\n(S=sumar,M=multiplicar,D=dividir,R=restar)\nSe operaran los numeros segun el caracter ingresado.")
operar=True
while operar:
    entrada=input("Ingrese un codigo de entrada para operar:\t").strip()
    if entrada[2].upper()=="S":
        resultado=int(entrada[0])+int(entrada[1])
    elif entrada[2].upper()=="D":
        resultado=int(entrada[0])/int(entrada[1])
    elif entrada[2].upper()=="M":
        resultado=int(entrada[0])*int(entrada[1])
    elif entrada[2].upper()=="R":
        resultado=int(entrada[0])-int(entrada[1])
    else:
        print("El codigo ingresado es incorrecto")
        continue
    print("Resultado: ", resultado)
    seguir=input("Desea dejar de operar?\n(y/n)\n").lower()
    if seguir=="y":
        operar=False