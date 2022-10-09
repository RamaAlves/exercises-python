""" Solicitar el ingreso de números al usuario y emitir un mensaje para determinar si es par o impar. 
El ciclo debe finalizar cuando el usuario ingresa 0 """

solicitarNumero=True

print("Averiguemos si es par o impar:")

while solicitarNumero:
    numero=int(input("Ingresar un numero:\t"))
    if numero==0:
        solicitarNumero=False
    elif numero%2 == 0:
        print("El numero ingresado es par")
    else:
        print("El numero ingresado es impar")

print("Adios!")