""" En una tienda de descuento por reciclado las personas que van a pagar el importe de su compra llegan a la caja y ofrecen tapitas para reciclar, 
de acuerdo a la cantidad que lleven en la caja le entregan un código de descuento que se aplicará sobre el total de su compra. Determinar la cantidad que 
pagara cada cliente desde que la tienda abre hasta que cierra. 
Se sabe que si el código de descuento es rojo se obtendrá un 40% de descuento; si es amarilla un 25% y si es blanca no obtendrá descuento. """

codigoBlanco=0 #sin descuento
codigoAmarillo=0 #25% off
codigoRojo=0 # 40%off
clientes=0
totalAPagar=0
listaDeClientes=[]
tiendaAbierta = True

while tiendaAbierta:
    importeAPagar=int(input("ingrese el monto a pagar expresado en AR$:\t"))
    codigoDescuento=int(str(input("ingrese el numero segun el codigo de descuento que corresponda:\n\t 1-Blanco\n\t2-Amarillo\n\t3-Rojo\n")).strip()[0])
    
    if codigoDescuento ==1:
        print("No tiene descuento")
        clientes+=1#actualizar acumulador de clientes
        codigoBlanco+=1#actualizar acumulador de codigo de descuento
        totalAPagar=importeAPagar#aplicando codigo de descuento
        print("Su total a pagar es de: $", totalAPagar) 
        listaDeClientes.append({"cliente":clientes, "subtotal":importeAPagar, "descuento":"0%", "total":totalAPagar})#creando respaldo de datos del cliente
    elif codigoDescuento==2:
        print("Su descuento es de un 25%")
        clientes+=1#actualizar acumulador de clientes
        codigoAmarillo+=1#actualizar acumulador de codigo de descuento
        totalAPagar=importeAPagar*0.75 #aplicando codigo de descuento
        print("Su total a pagar luego del descuento es de: $", totalAPagar)#luego de aplicar el descuneto
        listaDeClientes.append({"cliente":clientes, "subtotal":importeAPagar, "descuento":"25%", "total":totalAPagar})#creando respaldo de datos del cliente
    elif codigoDescuento==3:
        print("Su descuento es de un 40%")
        clientes+=1#actualizar acumulador de clientes
        codigoRojo+=1#actualizar acumulador de codigo de descuento
        totalAPagar=importeAPagar*0.60 #aplicando codigo de descuento
        print("Su total a pagar luego del descuento es de: $", totalAPagar)
        listaDeClientes.append({"cliente":clientes, "subtotal":importeAPagar, "descuento":"40%", "total":totalAPagar})#creando respaldo de datos del cliente
    else:
        print("Codigo incorrecto")
        continue

    preguntarCerrado=str(input("La tienda siegue abierta? \ty/n\n")).lower()
    if preguntarCerrado == "n":
        tiendaAbierta = False

#estadisticas del dia
verEstadisticas=str(input("Desea visualizar las estadisticas del dia?\ty/n\n"))

if verEstadisticas=="y":
    print("Mostrando estadisticas:")
    print("total de clientes en el dia:", clientes)
    print(f"{codigoBlanco} clientes no tuvieron descuento. Representan un {codigoBlanco*100/clientes}% del total de clientes")
    print(f"{codigoAmarillo} clientes tuvieron un 25% de descuento. Representan un {codigoAmarillo*100/clientes}% del total de clientes")
    print(f"{codigoRojo} clientes tuvieron un 40% de descuento. Representan un {codigoRojo*100/clientes}% del total de clientes")

#detalle de caja
verDetalleCaja = str(input("Desea visualizar el detalle de la caja?\ty/n\n"))

if verDetalleCaja=="y":
    totalEnCaja=0

    for cliente in listaDeClientes:
        print("cliente:", cliente["cliente"], "\ntotal sin descuentos: $", cliente["subtotal"], "\ndescuento aplicado: ", cliente["descuento"], "\npagó: $", cliente["total"])
        totalEnCaja+=cliente["total"]
        
    print("El total en caja al final del dia es: $", totalEnCaja)