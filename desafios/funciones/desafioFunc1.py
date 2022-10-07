""" 150 años es el tiempo que tarda una bolsa de plástico común en degradarse y una botella de PET puede tardar 1.000 años en desaparecer. 
Por otro lado los Envases de tetrabrik pueden tardar hasta 30 años en degradarse.
Un trozo de chicle tarda 5 años en degradarse. 
Se solicita una función para que dado el ingreso de un elemento, se solicite tipo: Bolsa de plástico, botella PET, 
envase tetrabrik o chicle, e imprima la cantidad de años que tarda en degradarse. """

elementosAnalizados=["bolsa de plastico", "botella de PET", "envase de tetrabrik", "chicle"]

def tiempoDeDegradacion(tipo):
    if tipo==1:
        print(f"Una {elementosAnalizados[0]} tarda 150 años en degradarse")
    elif tipo==2:
        print(f"Una {elementosAnalizados[1]} tarda 1000 años en degradarse")
    elif tipo==3:
        print(f"Un {elementosAnalizados[2]} tarda 30 años en degradarse")
    elif tipo==4:
        print(f"Un {elementosAnalizados[3]} tarda 5 años en degradarse")
    else:
        print("error de tipo")


print("tipos de elementos analizados:")
for elemento in elementosAnalizados:
    print(f"tipo {elementosAnalizados.index(elemento)+1}: {elemento}")
elementoADescartar= int(input("que tipo de elemento desea descartar:\n(ingrese el tipo en numeros)\n"))

tiempoDeDegradacion(elementoADescartar)