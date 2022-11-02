#try -except
#se prueva una expresion y si ocurre un error se pasa al bloque except

""" while(True):
    try:
        one = float(input("introduce un numero:\t"))
        two = 2
        print(f"{one}/{two} = {one/2}")
        break
    except:
        print("Ha ocurrido un error. Debe ingresar un numero.")
 """
#try - except - else
#se utiliza el esle para dar mas informacion acerca del resultado o modificar algo si todo funciona bien

""" while(True):
    try:
        one = float(input("introduce un numero:\t"))
        two = 2
        print(f"{one}/{two} = {one/2}")
    except:
        print("Ha ocurrido un error. Debe ingresar un numero.")
    else:
        print("todo funciono como se esperaba")
        break #importante, no olvidarse de romper la iteracion
 """
#try - except - else - finally
#finally se ejecuta siempre sin importar que suceda

""" while(True):
    try:
        one = float(input("introduce un numero:\t"))
        two = 2
        print(f"{one}/{two} = {one/2}")
    except:
        print("Ha ocurrido un error. Debe ingresar un numero.")
    else:
        print("todo funciono como se esperaba")
        break #importante, no olvidarse de romper la iteracion
    finally:
        print("Se ejecuta si o si") #siempre se ejecuta """

#Excepciones multiples
#Se puede guardar el error en una variable

""" try:
    one =input("Introduce un numero:\t") #no transformamos a numero
    print(5/one)
except TypeError:
    print("no se puede dividir un numero por una cadena")
except ValueError:
    print("debes introducir una cadena que sea un numero")
except ZeroDivisionError:
    print("el segundo argumento de una division no puede ser 0")
except Exception as e: #guardamos la excepcion como variable
    print(f"Ha ocurrido un error no previsto: {type(e).__name__}")
 """

# is -> raise genera un error
  
""" value= None
if value is None:
    print("Es nulo")
    raise ValueError("Error no se permite un valor nulo") #si necesito que especificamente esto arroje un error

print("sigue el programa") """

#assert 

try: #bloque de codigo a vigilar
    lista = [1,2,3,4,5,6]
    print(lista)
    while True:
        print("elemento a borrar ", lista[-1])
        lista.pop()
        assert len(lista)>1
        print(lista)
except AssertionError:
    print("error al intentar eliminar el elemento")
    print("la lista debe tener mas de un elemento")
    print("lista final: ",lista)