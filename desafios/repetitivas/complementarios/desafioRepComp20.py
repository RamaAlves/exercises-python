""" El Centro de Salud de Rosario tiene registradas N consultas médicas de menores. 
De cada consulta tiene como datos: la edad del menor y el día de visita. Los datos están ordenados en forma creciente por día. 
Proponer un fin de datos para cada día. Se desea conocer, para cada día, la edad promedio de pacientes y además el día en que se registró el máximo de pacientes.
 """
import random

consultas=[]#lista vacia donde se almacenaran las consultas
dia=1#set dia consulta
consultar=False #bandera del bucle while

cargarDatos=input("desea cargar datos de pacientes?\n(y/n)\n")#si se opta por no cargar pacientes se cargara la lista de consultas con valores aleatorios para testear la app.
if cargarDatos=="y":
    consultar=True
else:
    for i in range(100): #se genera de manera automatica datos de 100 consultas
        consulta=[random.randint(1,17),random.randint(1,30)]
        consultas.append(consulta)
    #print("lista desordenada",consultas)
    consultas.sort(key=lambda consulta:consulta[1])#ordenando la lista de consultas por dia, de menor a mayor

while consultar:
    edad=int(input("indique la edad del paciente:\t"))
    consulta=[edad,dia]
    consultas.append(consulta)
    finDia=input("finalizo el dia de carga?\n(y/n)\n")#si se finaliza el dia se actualiza el valor de dia pasando al dia siguiente
    if finDia=="y":
        dia+=1
    continuar=input("Desea continuar cargando consultas?\n(y/n)\n").lower()
    if continuar=="n":#condicional que actualiza la bandera del bucle while
        consultar=False;

#print("lista ordenada", consultas)
listaTotalPacientesXDia=[]
diaActual=consultas[0][1]
acumuladorEdad=0
pacientes=0
for consulta in consultas:
    dia=consulta[1]
    if dia==diaActual:
        acumuladorEdad+=consulta[0]
        pacientes+=1
        diaCargar=dia
    else:
        totalPacientesXDia=[]
        totalPacientesXDia.append(acumuladorEdad)
        totalPacientesXDia.append(diaCargar)
        totalPacientesXDia.append(pacientes)
        listaTotalPacientesXDia.append(totalPacientesXDia)
        acumuladorEdad=consulta[0]
        pacientes=1
        diaActual=diaCargar=consulta[1]
totalPacientesXDia=[]
totalPacientesXDia.append(acumuladorEdad)
totalPacientesXDia.append(dia)
totalPacientesXDia.append(pacientes)
listaTotalPacientesXDia.append(totalPacientesXDia)

#print("Lista acumulada",listaTotalPacientesXDia)

for totalPacientesXDia in listaTotalPacientesXDia:
    print(f"Día: {totalPacientesXDia[1]}\nLa edad promedio de los pacientes fue: {totalPacientesXDia[0]/totalPacientesXDia[2]}")

listaOrdenadaMasPacientesXDia=sorted(listaTotalPacientesXDia,key=lambda dia:dia[2], reverse=True)
#print("lista ordenada por cantidad de pacientes diarios (de mayor a menor):\t",listaOrdenadaMasPacientesXDia)
print(f"El dia {listaOrdenadaMasPacientesXDia[0][1]} hubo mayor cantidad de pacientes.\nFueron un total de {listaOrdenadaMasPacientesXDia[0][2]} pacientes.")