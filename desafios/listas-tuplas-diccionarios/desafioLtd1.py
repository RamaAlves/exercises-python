""" Escribir un programa que pregunte a diferentes personas cuánto conocen sobre contaminación del 1 al 10, 
almacene estos valores en una lista y los muestre por pantalla ordenados de menor a mayor.  """

#Solucion
""" 
conocimientoContaminacion=[]
preguntar=True

while preguntar:
    conocimiento=int(input("indique su nivel de conocimiento sobre contaminación (expresado en numeros del 1 al 10):\t"))
    conocimientoContaminacion.append(conocimiento)
    consulta=input("desea seguir preguntando\ty/n\n")
    if consulta=='n':
        preguntar= not preguntar

conocimientoOrdenado=sorted(conocimientoContaminacion)

print("lista ordenada: ",conocimientoOrdenado)
print("lista desordenada: ",conocimientoContaminacion)
 """
#resolucion con agregados... 
concocimientoContaminacion=[]
preguntar=True

while preguntar:
    encuestado=[]
    nombre= input("indique su nombre:\t")
    encuestado.append(nombre)
    estudios= input("indique su nivel de estudios maximo alcanzado:\n(primaria incompleta o completa, secunadria incompleta o completa, terciario o universitario incompleto o completo\n")
    encuestado.append(estudios)
    conocimiento=int(input("indique su nivel de conocimiento sobre contaminación (expresado en numeros del 1 al 10):\t"))
    encuestado.append(conocimiento)
    concocimientoContaminacion.append(encuestado)
    consulta=input("desea seguir preguntando\ty/n\n")
    if consulta=='n':
        preguntar= not preguntar

concocimientoContaminacion.sort(key=lambda conocimiento: conocimiento[2])
print("lista ordenada de los que menos saben a los que mas saben:")
for individuo in concocimientoContaminacion:
    print(f"nombre: {individuo[0]}\tconocimientos sobre contaminacion: {individuo[2]}\t nivel de estudios alcanzado: {individuo[1]}")

