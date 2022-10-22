""" Ejercicio 3: Calculadora de envío
Un minorista en línea proporciona una forma de envío urgente de $ 10.95 para el primer 
elemento y $ 2.95 para cada segundo elemento posterior. 
Escriba una función que tome el número de elementos en el pedido como su único parámetro. 
Devuelva los gastos de envío del pedido como resultado de la función. Incluya un programa principal 
que lea la cantidad de artículos comprados al usuario y muestre los gastos de envío. """

def calcular_envio(articulos):
    envioUrgente= 10.95
    extra=2.95
    if articulos==1:
        return envioUrgente
    elif articulos>1:
        costoExtra=(articulos-1)*extra
        costoTotal=envioUrgente+costoExtra
        return costoTotal
    else:
        return print("Error")