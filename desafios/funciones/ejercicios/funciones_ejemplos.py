def funcion_saludo(usuario=None):  #def (palabra reservada) funcion_saludo (nombre de la funcion) usuario(argumento)
    """ Esta funcion imprime un saludo recibiendo un argumento que se imprimira como nombre"""
    print("hola ", usuario)

funcion_saludo("Ramiro") #invocacion de la funcion
funcion_saludo(usuario="Fernando") #pasando parametro por nombre
funcion_saludo()#lanza la excepcion TypeError porque la llamada se realizo sin argumento. para evitar esto se puede definir el argumento como None
def indeterminados(*args): #argumentos indeterminados se reciben por posicion usando *
    for arg in args:
        print(arg)
indeterminados(5,"hola", [21,1,15])

def otrosIndeterminados(**kwargs): #argumentos indeterminados se reciben por posicion usando *
    for kwarg in kwargs:
        print(kwarg, "=>", kwargs[kwarg])

otrosIndeterminados(n=5,c="casa",l=[1,2,3,4])

def todoIndeterminado(*args, **kwargs):
    total = 0
    for arg in args:
        total+=arg
        
    print("Total =>",total)
    for kwarg in kwargs:
        print(kwarg, "=>", kwargs[kwarg])

todoIndeterminado(5,3,1,2,c="hola ", h="bye!")

saludo="Hola "#variable global
def var_local_y_global(b):
    b+="Tu" #variable local
    print(b)#variable local
    print(saludo)#variable global

var_local_y_global(saludo)

#llamada a una funcion dentro de otra

def mensaje():
    return "hola mundo"

def saludar(nombre,saludo="Hola"):
    print(mensaje())
    print(saludo,nombre)

saludar("Pablo")

#como saber si la funcion existe
def mensaje(nombre):
    return "hola "+ nombre

def funcion_de_llamada(nombre, funcion=""):
    if funcion in globals():
        if callable(globals, funcion, nombre):
            funcion(nombre)
    else:
        print("la funcion no existe!")