""" Diseñar un programa que permita calcular el total de una compra, ingresando cantidad y precio de los productos. 
El programa debe estar preparado para que el ingreso de los datos se produzca hasta que el usuario lo desee. """

agregarProductos=True
listaDeProductos=[]
total=0
while agregarProductos:
    producto=[]
    producto.append(input("Nombre del producto:\t"))
    producto.append(float(input("Precio por unidad:\t")))
    producto.append(int(input("Cantidad:\t")))
    producto.append(producto[1]*producto[2])
    listaDeProductos.append(producto)
    continuar=input("Desea agregar más productos?\n(y/n)\n").lower()
    if continuar=="n":
        agregarProductos=False

print("Producto\tPrecio Unitario\tCantidad\tPrecio")
for producto in listaDeProductos:
    print(f"{producto[0]}\t\t${producto[1]}\t\t{producto[2]}\t\t${producto[3]}")
    total+=producto[3]

print("El total de la compra es: $",total)