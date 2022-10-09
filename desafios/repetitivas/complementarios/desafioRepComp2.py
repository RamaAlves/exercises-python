""" Desarrollar una solución que calcule la suma de los cuadrados de los n primeros números naturales: 1 + 2^2 + 3^2 +… + n2. """
print("Calculemos la suma de los cuadrados de los n primeros números naturales:\n")
numero=int(input("Ingrese un numero:\t"))
contador=1
sumaDeCuadrados=0

while contador<=numero:
    sumaDeCuadrados+=(contador**2)
    contador+=1

print(sumaDeCuadrados)