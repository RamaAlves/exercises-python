""" un diccionario es un conjunto de datos ordenados por pares clave valor 
    se pueden almacenar todo tipo de datos inclusive andiar diccionarios
    se pueden agregar, modificar o eliminar elementos.
    los elementos dentro del diccionario estan desordenado
    las claves son inmutables. no pueden ser listas
    {
        clave:valor,
        clave2:valor2
        }

    las claves son unicas
    no tienen ordenado
    son mutables, pueden alterarse durante la ejecucion del programa
    si una clave se repite, toma el ultimo valor declarado

"""
#creacion de dict

dict_vacio={}
print(f"esto es un diccionario {dict_vacio}")
print(f"es del tipo de dato {type(dict_vacio)}")

otro_dict= dict()
print(f"esto es un diccionario {otro_dict}")
print(f"es del tipo de dato {type(otro_dict)}")

#diccionario con valores
usuario={
    'nombre':'Juan Perez',
    'edad':30,
    'curso': 'Programacion Web',
    'domicilio':{
        'calle':'Calle Falsa 123',
        'localidad':'Saenz Peña',
        'provincia':'Chaco',
    },
    'nivel':'basico'
}
print(usuario)

#para acceder a un elemento utilizo las claves
nombre_usuario=usuario['nombre']
print(f"nombre de usuario")
#para acceder a un diccionario anidado
calle_usuario=usuario['domicilio'].get('calle')
#o para acceder a cualquier campo
domicilio_usuario=usuario.get('domicilio').get('localidad')
#                                       DEVOLUCION SI LA CLAVE NO EXISTE
deporte_usuario=usuario.get('deporte','la clave no existe')

#modificar datos
#actualizar datos
usuario['curso']='base de datos'

#agregar un elemento
usuario['telefono']='321564978'

#eliminar datos
del usuario['telefono']


#comprobar existencia
existe= 'domicilio' in usuario

no_existe= 'domicilio' not in usuario


#devuelve claves
usuario_keys=usuario.keys()

#devuelve los valores almacenados
usuario_values = usuario.values()

#items devuelve pares clave valor
usuario_items=usuario.items()

#setDefault muestra el valor que pose una clave si no existe la agrega al diccionario
persona={'name':'Paul','edad':22}

#si la clave existe
edad=persona.setdefault('edad')
#si la clave no existe
pais=persona.setdefault('pais')
#valor por defecto
profesion=persona.setdefault('profesion', 'trabajo')

#fromkeys crea un diccionario con las claves pasadas como parametros

llaves=('a','e','i','o','u')

vocales=dict.fromkeys(llaves)
print(vocales)
#valores por defecto
frutas=('manzana','pera','naranja')
values=(100,200)
precios=dict.fromkeys(frutas,values)

#update agrega elementos si no existen y si existe lo sobrescribe

#pop devuelve y elimina del diccionario el valor almacenado en la clave pasada como parametro. si el valor no existe se puede pasar un valor por defecto

#popitem elimina el ultimo par clave valor

# copy() copia el diccionario permitiendo modificarlo sin afectar al original

#len() recibe el diccionario como parametro

#max() devuelve la maxima clave siempre que sean comparables

#min() devuelve la minima clave siempre que sean comparables

#sum() devuelve la suma de las claves siempre y cuando las mismas se puedan sumar