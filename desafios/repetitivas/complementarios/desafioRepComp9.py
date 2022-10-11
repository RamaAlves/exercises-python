""" Un censador recopila ciertos datos aplicando encuestas para el último Censo Nacional de Población y Vivienda. 
Desea obtener de todas las personas que alcance a encuestar en un día, 
que porcentaje tiene estudios de primaria, secundaria, carrera técnica, estudios profesionales y estudios de posgrado. """

encuestados=[]
encuestar=True
datosEstadistica=[0,0,0,0,0,0] #[0]total, [1]primaria, [2]secundaria, [3]profesional, [4]posgrado, [5]carreratecnica

while encuestar:
    persona={}
    nombre=input("Ingrese el nombre del encuestado:\t").capitalize()
    print("Opciones de nivel de estudios completos:\n1-primaria\n2-secundaria\n3-profesional\n4-posgrado")
    estudios=int(input("ingrese el nivel de estudios que posee:\n"))
    if estudios>0 and estudios<5:
        persona['nombre']=nombre
        persona["estudios"]=estudios
    else:
        print("La opcion ingresada es incorrecta")
        continue
    tecnico=int(input("Realizo carrera tecnica?\n(Presione 1 si lo realizó, 0 si no lo realizó)\n"))
    if tecnico==1:
        cargar=persona.get("nombre", "cargar")
        if cargar=="cargar":
            persona["nombre"]=nombre
        persona["carreraTecnica"]=tecnico
    encuestados.append(persona)
    continuar=input("Desea finalizar la encuesta?\n(presione 'y' para finalizar la carga)\n").lower()
    if continuar=="y":
        encuestar=False

for encuestado in encuestados:
    datosEstadistica[0]+=1
    if encuestado.get("estudios",False)==1:
        datosEstadistica[1]+=1
    elif encuestado.get("estudios",False)==2:
        datosEstadistica[1]+=1
        datosEstadistica[2]+=1
    elif encuestado.get("estudios",False)==3:
        datosEstadistica[1]+=1
        datosEstadistica[2]+=1
        datosEstadistica[3]+=1
    else:
        datosEstadistica[1]+=1
        datosEstadistica[2]+=1
        datosEstadistica[3]+=1
        datosEstadistica[4]+=1
    if encuestado.get("carreraTecnica",False):
        datosEstadistica[5]+=1
    print(encuestado)

print("Mostrando estadisticas:")
print(f"De un total de {datosEstadistica[0]} encuestados:\nUn {(datosEstadistica[1]*100)/datosEstadistica[0]}% finalizó la primaria\nUn {(datosEstadistica[2]*100)/datosEstadistica[0]}% finalizó la secundaria\nUn {(datosEstadistica[5]*100)/datosEstadistica[0]}% realizó una carrera tecnica\nUn {(datosEstadistica[3]*100)/datosEstadistica[0]}% tiene estudios profesionales\nUn {(datosEstadistica[4]*100)/datosEstadistica[0]}% estudió al menos un posgrado")

print(encuestados)