""" Ejercicio 22: ¿Es un palíndromo?

Escriba una función llamada es_palindromo que devuelva True si una cadena dada es un palíndromo. 
Un palíndromo es una cadena que se escribe igual hacia atrás o hacia adelante. 
Por ejemplo, radar es palíndromo. Use la función en un programa principal y pruebe su código en varios 
valores diferentes. """


def es_palindromo(cadena):
    copiaCadena=cadena.lower().strip()
    listaCopia=list(copiaCadena)
    listaCopia.reverse()
    nuevaCadena = "".join(listaCopia)
    if copiaCadena == nuevaCadena:
        return True
    else:
        return False
