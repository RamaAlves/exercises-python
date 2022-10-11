""" Una pizzería, vende sus pizzas en tres tamaños: pequeña, mediana; y grandes. 
Una pizza puede ser sencilla (con sólo salsa y carne), o con ingredientes extras, tales como pepinillos, champiñones o cebollas. 
Desarrolle una solución que calcule el precio de venta de una pizza, dándole el tamaño y el número de ingredientes extras. 
El precio de venta será 1.5veces el costo total, que viene determinado por el tamaño, más el número de ingredientes. 
En particular el costo total se calcula sumando:

- un costo fijo de preparación.
- un costo variable que es proporcional al tamaño de la pizza.
- un costo adicional por cada ingrediente extra (por simplicidad se supone que cada ingrediente extra tiene el mismo costo). """

pedidos=[[3,3],[2,0],[1,2],[3,1],[2,3]]
costoFijo=100
ingredienteExtra=15
precioSize=[80,110,140]
cont=1

for pedido in pedidos:
    precioPedido=0
    size=""
    if pedido[0]==1:
        precioPedido=costoFijo+precioSize[0]+(ingredienteExtra*pedido[1])
        size="pequeña"
    elif pedido[0]==2:
        precioPedido=costoFijo+precioSize[1]+(ingredienteExtra*pedido[1])
        size="mediana"
    elif pedido[0]==3:
        precioPedido=costoFijo+precioSize[2]+(ingredienteExtra*pedido[1])
        size="grande"
    else:
        print("error")
    precioVenta=precioPedido*1.5
    print(f"Pedido {cont}:\nTamaño: {size}\nIngredientes extra:{pedido[1]}\nValor: ${precioVenta}")
    cont+=1