""" Hacer un programa que imprima el nombre de un artículo, clave, 
precio original y su precio con descuento. El descuento lo hace en base a la clave, 
si la clave es 01 el descuento es del 10% y si la clave es 02 el descuento en del 20% (solo existen dos claves). """

articulos= [["fideos","02",180], ["maple de huevo","01",500], ["arvejas","02",150]]

for articulo in articulos:
    if articulo[1]=="01":
        descuento= articulo[2]*0.9
        print(f"producto: {articulo[0]}\ncodigo: {articulo[1]}\nprecio: ${articulo[2]}\nprecio con descuento (10%): ${descuento}")
    elif articulo[1]=="02":
        descuento= articulo[2]*0.8
        print(f"producto: {articulo[0]}\ncodigo: {articulo[1]}\nprecio: ${articulo[2]}\nprecio con descuento (20%): ${descuento}")
    else:
        print("El codigo indicado es incorrecto")
