# la sentencia if es un condicional. si la condicion declarada se cumple se entra dentro del ciclo indicado
# la sentencia elif es una condicional el cual se utiliza si deseo evaluar mas de una condicion luego del if
# para la ultima evaluacion se utiliza else. else no lleva condicion, solo se evalua si todo lo demas no ocurre
# las condiciones siempre empiezan con if y finalizan con else. Si necesito mas condiciones utilizo elif en medio.

importe = int(input("Ingrese el monto total de la compra"))

if importe>1500:
    print ("Descuento del 30%")
elif importe>1000:
    print ("Descuento del 20%")
elif importe>500:
    print ("Descuento del 10%")
else:
    print("Descuento del 5%")