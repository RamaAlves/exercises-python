""" Nos han pedido desarrollar una aplicación móvil para reducir comportamientos inadecuados para el ambiente.
a) Te toca escribir un programa que simule el proceso de Login. Para ello el programa debe preguntar al usuario la contraseña,
 y no le permita continuar hasta que la haya ingresado correctamente.
b) Modificar el programa anterior para que solamente permita una cantidad fija de intentos.  """

password = "1"

""" passInput=str(input("ingrese la contraseña: \t")).lower() """

""" while password != passInput:
    print("Contraseña incorrecta. Reingrese la contraseña")
    passInput=input(str("ingrese la contraseña: \t")).lower()
print("Ingresaste") """

usuario="1"
contador=0
passInput=None
userInput=None
while contador<3:
    userInput=str(input("ingrese la contraseña: \t")).lower()
    passInput=str(input("ingrese la contraseña: \t")).lower()
    contador+=1
    if (usuario== userInput and password == passInput):
        print("Ingresaste")
        break
    else:
        print("Usuario y contraseña incorrectos.")
else:
        print("Superaste el numero maximo de intentos. Usuario bloqueado")