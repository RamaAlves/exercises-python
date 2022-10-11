""" Realizar un programa que calcule y muestre la suma de los múltiplos de 5 comprendidos entre dos valores A y B. 
El programa no permitirá introducir valores negativos para A y B y verificará que A es menor que B. Si A es mayor que B, se deben intercambiar los valores. """

rango=[]
sumatoriaMultiplos5=0
listaMultiplos5=[]

print("Se calcularán los multiplos de 5 comprendidos entre los valores ingresados.\nNo se aceptan numeros negativos.\nEl primer número debe ser menor que el segundo\nSi el primer numero es mayor que el segundo el orden de los mismos se invertira.")
numero1=int(input("Ingrese el primer número:\t"))
while numero1<0:
    print("No se aceptan números negativos.")
    numero1=int(input("Ingrese el primer número:\t"))
rango.append(numero1)
numero2=int(input("Ingrese el segundo número:\t"))

while numero2<0:
    print("No se aceptan números negativos.")
    numero2=int(input("Ingrese el segundo número:\t"))

rango.append(numero2)
rango.sort()

for numero in range(rango[0],(rango[1]+1)):
    if numero%5==0:
        sumatoriaMultiplos5+=numero
        listaMultiplos5.append(numero)

print("La sumatoria de los multiplos de 5 es: ",sumatoriaMultiplos5)
print("Los multiplos de 5 entre el rango establecido es: ",listaMultiplos5)