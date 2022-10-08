""" Un comercio ofrece un descuento del 15% sobre el total de la compra si esta supera los $1000. 
Obtenga para determinado cliente cuánto deberá pagar finalmente por su compra y el descuento obtenido, si es que corresponde. """

subtotal= float(input("ingrese el total de la compra:\t"))

if subtotal>1000:
    descuento=subtotal*0.15#calculando descuento
    total=subtotal-descuento#aplicando el 15% de descuento
    print(f"El total de la compra es ${subtotal}. Usted accedio a un descuento de un 15% (${descuento}). Debe abonar ${total}")
else:
    print(f"Usted no accedio a ningun descuento. El total de su compra es ${subtotal}.")