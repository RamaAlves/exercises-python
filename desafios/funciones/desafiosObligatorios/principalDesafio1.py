""" 150 años es el tiempo que tarda una bolsa de plástico común en degradarse y una botella de PET puede tardar 1.000 años en desaparecer. 
Por otro lado los Envases de tetrabrik pueden tardar hasta 30 años en degradarse.
Un trozo de chicle tarda 5 años en degradarse. 
Se solicita una función para que dado el ingreso de un elemento, se solicite tipo: Bolsa de plástico, botella PET, 
envase tetrabrik o chicle, e imprima la cantidad de años que tarda en degradarse. """

from desafioFunc1 import tiempoDeDegradacion

elementosAnalizados=["bolsa de plastico", "botella de PET", "envase de tetrabrik", "chicle"]

""" def tiempoDeDegradacion(tipo):
    if tipo==1:
        return 150
    elif tipo==2:
        return 1000
    elif tipo==3:
        return 30
    elif tipo==4:
        return 5
    else:
        return print("error de tipo")
 """

print("tipos de elementos analizados:")
for elemento in elementosAnalizados:
    print(f"tipo {elementosAnalizados.index(elemento)+1}: {elemento}")
elementoADescartar= int(input("que tipo de elemento desea descartar:\n(ingrese el tipo en numeros)\n"))

print(f"Una {elementosAnalizados[elementoADescartar]} tarda {tiempoDeDegradacion(elementoADescartar)} años en degradarse") 