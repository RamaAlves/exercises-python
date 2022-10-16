"""  Dados los datos de un municipio: zona, sexo y edad de cada uno de sus habitantes, encontrar:

a) porcentaje de varones menores de 15 años para cada zona
b) porcentaje de varones menores de 15 años para todo el municipio

Los datos vienen ordenados por zona.Con dato de zona igual a 0, se indica el fin. """

#contadores
varones=0
varonesMenores15=0
varonesMenoresZona1=0
varonesMenoresZona2=0
varonesMenoresZona3=0
varonesMayores15=0
varonesMayoresZona1=0
varonesMayoresZona2=0
varonesMayoresZona3=0


mujeres=0
mujeresMenores15=0
mujeresMenoresZona1=0
mujeresMenoresZona2=0
mujeresMenoresZona3=0
mujeresMayores15=0
mujeresMayoresZona1=0
mujeresMayoresZona2=0
mujeresMayoresZona3=0

#listaGenerada
#datosMunicipio=[] #[zona,sexo,edad] 
datosMunicipio=[[1,"v",25],[1,"v",14],[2,"v",23],[2,"v",23],[2,"v",23],[2,"v",13],[3,"v",15],[3,"v",12],[3,"v",12],[1,"v",19],[1,"v",10],[2,"v",24],[2,"v",8],[3,"v",10],[3,"v",10],[1,"m",25],[1,"m",14],[1,"m",14],[2,"m",23],[2,"m",13],[3,"m",15],[3,"m",15],[3,"m",15],[3,"m",12]] #Test

while True:
    dato=[]
    zona=int(input("Ingrese la zona de residencia:\t"))
    
    if zona==0:
        print("Procesando datos...")
        break

    dato.append(zona)
    sexo=input("Indique el sexo del individuo:\n(v/m)\n")
    dato.append(sexo)
    edad=int(input("Indique la edad del individuo:\t"))
    dato.append(edad)
    datosMunicipio.append(dato)

print("Mostrando resultados:")

for dato in datosMunicipio:
    if dato[1].lower()=="v":
        varones+=1
        if dato[2]<15:
            varonesMenores15+=1
            if dato[0]==1:
                varonesMenoresZona1+=1
            elif dato[0]==2:
                varonesMenoresZona2+=1
            elif dato[0]==3:
                varonesMenoresZona3+=1
            else:
                print("error")
        else:
            varonesMayores15+=1
            if dato[0]==1:
                varonesMayoresZona1+=1
            elif dato[0]==2:
                varonesMayoresZona2+=1
            elif dato[0]==3:
                varonesMayoresZona3+=1
            else:
                print("error")
    elif dato[1].lower()=="m":
        mujeres+=1
        if dato[2]<15:
            mujeresMenores15+=1
            if dato[0]==1:
                mujeresMenoresZona1+=1
            elif dato[0]==2:
                mujeresMenoresZona2+=1
            elif dato[0]==3:
                mujeresMenoresZona3+=1
            else:
                print("error")
        else:
            mujeresMayores15+=1
            if dato[0]==1:
                mujeresMayoresZona1+=1
            elif dato[0]==2:
                mujeresMayoresZona2+=1
            elif dato[0]==3:
                mujeresMayoresZona3+=1
            else:
                print("error")
    else:
        print("error")

print("total de personas cargadas: ", len(datosMunicipio))
print(f"Total de varones: {varones}\nVarones menores de 15 años: {(varonesMenores15*100)/varones}%")
print(f"De estos un {(varonesMenoresZona1*100)/varonesMenores15}% son de la zona 1\nUn {(varonesMenoresZona2*100)/varonesMenores15}% son de la zona 2\nUn {(varonesMenoresZona3*100)/varonesMenores15}% son de la zona 3")
print(f"Varones mayores de 15 años: {(varonesMayores15*100)/varones}%")
print(f"De estos un {(varonesMayoresZona1*100)/varonesMayores15}% son de la zona 1\nUn {(varonesMayoresZona2*100)/varonesMayores15}% son de la zona 2\nUn {(varonesMayoresZona3*100)/varonesMayores15}% son de la zona 3")
print(f"Total de mujeres: {mujeres}\nMujeres menores de 15 años: {(mujeresMenores15*100)/mujeres}%")
print(f"De estos un {(mujeresMenoresZona1*100)/mujeresMenores15}% son de la zona 1\nDe estos un {(mujeresMenoresZona2*100)/mujeresMenores15}% son de la zona 2\nDe estos un {(mujeresMenoresZona3*100)/mujeresMenores15}% son de la zona 3")
print(f"Mujeres mayores de 15 años: {(mujeresMayores15*100)/mujeres}%")
print(f"De estos un {(mujeresMayoresZona1*100)/mujeresMayores15}% son de la zona 1\nDe estos un {(mujeresMayoresZona2*100)/mujeresMayores15}% son de la zona 2\nDe estos un {(mujeresMayoresZona3*100)/mujeresMayores15}% son de la zona 3")