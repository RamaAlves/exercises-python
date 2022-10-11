""" Calcular el monto a pagar por cada cliente y total recaudado en una estación de servicio. 
Debe diseñar un programa que permita monto por cliente y el total recaudado por la gasolinera, tomando en cuenta lo siguiente:

• El precio del litro es para el Tipo A $50, para el Tipo B $ 55 y para el Tipo C $60
• El programa finaliza cuando se introduce una D como tipo de gasolina. """

print("Los tipos de gasolina disponibles son:\nTipo A\tvalor: $50\nTipo B\tvalor: $55\nTipo C\tvalor: $60")
tipo=input("Introduzca el tipo de gasolina a cargar:\n(El programa finaliza con 'D')\n\t").strip().capitalize()[0]
caja=[]

while tipo !="D":
    total=None
    if tipo=="A":
        litros=int(input("Cuantos litros desea cargar?\t"))
        total=litros*50
        caja.append(total)
        print("Su total a pagar es de: $",total)
    elif tipo=="B":
        litros=int(input("Cuantos litros desea cargar?\t"))
        total=litros*55
        caja.append(total)
        print("Su total a pagar es de: $",total)
    elif tipo=="C":
        litros=int(input("Cuantos litros desea cargar?\t"))
        total=litros*60
        caja.append(total)
        print("Su total a pagar es de: $",total)
    else:
        print("Disculpe. No contamos con ese tipo de gasolina.")
    tipo=input("Introduzca el tipo de gasolina a cargar:\n(El programa finaliza con 'D')\n\t").strip().capitalize()[0]

totalRecaudado=0
for dinero in caja:
    totalRecaudado+=dinero
print("El total recaudado es: $",totalRecaudado)