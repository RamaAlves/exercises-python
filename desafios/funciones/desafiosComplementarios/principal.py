from hipotenusa import calcularHipotenusa
from calculadoraEnvios import calcular_envio
from esNumeroPrimo import numero_primo
from esPalindromo import es_palindromo


"""Ejercicio complementario 3: calculadora de envios """

""" print("Esta funcion calcula el costo de envio de los articulos comprados")
articulos=int(input("Ingrese la cantidad de articulos solicitados:\t"))

costo=calcular_envio(articulos)

if costo =="Error":
    print("La cantidad de articulos ingresada es incorrecta")
else:
    print(f"El costo de su envio es ${costo}. Ud a comprado {articulos} articulos en total.")
 """
""" 
print("Esta funcion recibe dos catetos y retorna la hipotenusa") """

""" Es número primo  """
""" 
print("Este programa recibe un numero e indica si es primo o no")
numero=int(input("Indique el numero que desea comprobar:\t"))

if numero_primo(numero):
    print("El numero es primo")
else:
    print("El numero no es primo")
 """
""" ¿Es un palíndromo?"""

print("Este programa revisa si una palabra ingresada es palindromo o no")
palindromo=input("ingrese la palabra que desea comprobar:\t")
if es_palindromo(palindromo):
    print("La palabra ingresada es un palindromo")
else:
    print("La palabra ingresada no es un palindromo")