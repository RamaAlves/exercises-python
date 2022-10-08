""" Una distribuidora de libros vende a librerías y a particulares. Aplica bonificaciones por cantidad según el siguiente criterio:
    i.      a librerías: hasta 24 unidades, el 20%; más de 24 unidades, el 25%.

    ii.      a particulares: menos de 6 unidades, nada; desde 6 hasta 18 unidades, el 5% y más de 18 unidades, el 10%.

El tipo de cliente está codificado así: 'L' para librerías, 'P' para particular. Dado el importe bruto de una compra de libros, 
el tipo de cliente de que se trata y la cantidad total pedida por el mismo, determinar el importe bruto bonificado. """

tipoCliente=input("Indique si es libreria o particular:\n('L' para librerias y 'P' para paraticulares)\n\n").strip().capitalize()[0]

if tipoCliente=="L":
    libros=int(input("Indique la cantidad de libros que compra:\t"))
    if libros>0 and libros<=24:
        print("Su descuento es del 20%.")
    elif libros>24:
        print("Su descuento es del 25%.")
    else:
        print("Debe comprar un libro como mínimo.")
elif tipoCliente=="P":
    libros=int(input("Indique la cantidad de libros que compra:\t"))
    if libros>=6 and libros<=18:
        print("Su descuento es de un 5%.")
    elif libros>18:
        print("Su descuento es de un 10%.")
    else:
        print("Usted no tiene descuentos disponibles.")
else:
    print("Tipo de cliente incorrecto.")