""" Crea un diccionario donde la clave sea el nombre de biólogos y el valor sea el email (no es necesario validar). 
Tendrás que ir pidiendo contactos hasta el usuario diga que no quiere insertar mas. No se podrán insertar nombres repetidos. """

#validacion sencilla

""" registroBiologos={}
ingresar= True #bandera
while ingresar:
    nombre=str(input("ingrese el nombre del biologo:\t"))
    email=str(input("ingrese el e-mail del biologo:\t"))
    while "@" not in email: #validacion de mail se podria usar una expresion regular para este paso
        print("correo inválido. reintente:")
        email=str(input("ingrese el e-mail del biologo:\t"))
    registroBiologos[nombre]=email
    consulta=input("desea ingresar mas biologos?\ty/n\t")
    if consulta =="n":
        ingresar=False

print(registroBiologos)
 """

#validacion usando expresion regular
import re

registroBiologos={}
ingresar= True#bandera

#validar mail
def es_correo_valido(correo):
    expresion_regular = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
    return re.match(expresion_regular, correo) is not None
mail=input("ingrese un mail:\t")

while ingresar:
    nombre=str(input("ingrese el nombre del biologo:\t"))
    email=str(input("ingrese el e-mail del biologo:\t"))
    while not es_correo_valido(email): #validacion de mail con una expresion regular
        print("correo inválido. reintente:")
        email=str(input("ingrese el e-mail del biologo:\t"))
    registroBiologos[nombre]=email

    seguir=input("desea ingresar mas biologos?\ty/n\t")
    if seguir =="n":
        ingresar=False

print(registroBiologos)