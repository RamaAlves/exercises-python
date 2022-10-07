""" Se inicia una campaña de recolección de colillas de cigarrillos en los barrios.
Realizá un programa que permita registrar cantidad de colillas recolectadas por un número determinado de personas. 
Luego obtener estadísticas al respecto informando porcentaje de personas que han encontrado menos de 100 colillas, más de 100 y menos de 200, más de 200 colillas. """

menos100=0
entre100y200=0
mas200=0
recolectores=0

agregarPersona = True #bandera
cantidadDeRecolectores= int(input("ingrese la cantidad de recolectores:\t"))

while agregarPersona:#con bandera #recolectores<cantidadDeRecolectores: #con acumulador
    colillas=int(input("ingrese la cantidad de colillas que juntó el recolector:\t"))
    recolectores+=1
    if colillas<100:
        menos100+=1
    elif colillas<200:
        entre100y200+=1
    else:
        mas200+=1

    preguntar=str(input("Desea ingresar mas recolectores? \ty/n\n")).lower()
    if preguntar == "n":
        agregarPersona = False

print("Mostrando estadisticas:")
print("total de recolectores", recolectores)
print(f"{menos100} personas juntaron menos de 100 colillas. Representan un {menos100*100/recolectores}% del total de recolectores")
print(f"{entre100y200} personas juntaron mas de 100 menos de 200 colillas. Representan un {entre100y200*100/recolectores}% del total de recolectores")
print(f"{mas200} personas juntaron menos de 100 colillas. Representan un {mas200*100/recolectores}% del total de recolectores")