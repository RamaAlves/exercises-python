""" Crea una tupla con los factores que más afectan a los mares. Luego para jugar con niños y niñas, 
aprendiendo sobre contaminación del agua crea un programa que pida números, si el numero esta entre 1 y la longitud máxima de la tupla, 
muestra el contenido de esa posición sino muestra un mensaje de error.
El programa termina cuando el usuario introduce un cero. """

afectaAlMar= ("bolsas de plastico", "petroleo", "quimicos toxicos", "basura")

print("contaminantes del mar:")
print("escribe un numero y si tienes suerte veras un contaminante del mar")
print ("para finalizar presiona 0")
numero=int(input("ingresa un numero para jugar:\n(el programa finaliza con 0)\n\n"))
while numero != 0:
    if numero <= len(afectaAlMar):
        print (afectaAlMar[numero-1])
    else:
        print("error: numero fuera de rango.")
    numero=int(input("ingresa un numero para jugar:\n(el programa finaliza con 0)\n\n"))