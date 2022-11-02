""" similares a las listas pero estas son inmutables y ordenadas. su rendimiento es mucho mas rapido"""

#se crea con

nueva_tupla=()
print(nueva_tupla)
print(type(nueva_tupla))

otra_tupla=tuple()
print(otra_tupla)
print(type(otra_tupla))

#empaquetado de tuplas
dias="lunes","martes","miercoles", "jueves", "viernes"

#desempaquetado
l,m,mi,j,v=dias

l,m,mi,j,v,*s=dias

print(dias)
print("dias: ",type(dias))
print(l)
print(m)
print(mi)
print(j)
print(v)
print(s)
 
dias="lunes","martes","miercoles", "jueves", "viernes", "sabado", "domingo"

l,m,mi,j,v,*s=dias

print(l)
print(m)
print(mi)
print(j)
print(v)
print(s)

tupla_mezcla=(1,5,"hola",2.7)
print(tupla_mezcla)
print(type(tupla_mezcla))

#acceder por indice
lunes=dias[0]
print(lunes)

#ultimo elemento
ultimo=dias[-1]
print(ultimo)

#como acceder a un elemento dentro de una tupla
mix=("perro","gato","loro",("canario","yaguarete"),"saltamontes")
elemento1=mix[0]
elemento1_indice2=mix[0][2]
elemento4_indice1=mix[3][1]
elemento4_indice1_indice0=mix[3][1][0]
print()

cursos=("excel","word","access")
sub_cursos=cursos[:1]
print(cursos)
print(sub_cursos)

#recorrer
for curso in cursos:
    print(curso)

#enumerate
for indice, curso in enumerate(cursos):
    print(f"en el indice{indice}: {curso}")

edades=(45,82,62,45)
famosos=("arturo","jaime","juan")

for edad, famoso in zip(edades, famosos):
    print(f"{famoso} tiene {edad}")

#in y not in
print(55 in edades)
print(45 in edades)
print(55 not in edades)
print(45 not in edades)

#count()
art=famosos.count("arturo")
print(art)

#ordenar

#index

#len

#max

#min

#zip
tupla=(1,2,3,4,5)
lista=["a","b","c","d"]
zipthis=zip(tupla, lista)
print