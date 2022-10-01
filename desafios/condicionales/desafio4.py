""" Tenemos que decidir entre 2 recetas ecológicas. Los ingredientes para cada tipo de receta aparecen a continuación.
Ingredientes comunes: Verduras y berenjena.
Ingredientes Receta 1: Lentejas y apio.
Ingredientes Receta 2: Morrón y Cebolla..
Escribir un programa que pregunte al usuario que tipo de receta desea, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. 
Solo se puede eligir 3 ingrediente (entre la receta elegida y los comunes.) y el tipo de receta. Al final se debe mostrar por pantalla la receta elegida y todos los ingredientes. """

print ("Debe elegir un tipo de receta\n\nReceta 1: lentejas y apio\nReceta 2: Morrón y cebolla")
print ("Siempre tendrá disponible los ingredientes comunes:\nVerduras y Berenjenas")
receta1= ["lentejas", "apio","verduras", "berenjenas"]
receta2= ["morron", "cebolla", "verduras", "berenjenas"]

tipo_receta = int(input("Elija su receta:\n"))

#Opcion 1
 
if tipo_receta==1:
    print("Usted eligio la receta ", tipo_receta)
    print(f"Sus opciones son: \n1:{receta1[0]} \n2:{receta1[1]} \n3:{receta1[2]} \n4:{receta1[3]}")
    ingrediente_a_eliminar= int(input("Seleccione el ingrediente que no desea usar:\n"))-1
    if receta1.len>=ingrediente_a_eliminar:
        receta1.remove(receta1[ingrediente_a_eliminar])
        print(f"Usted eligio los siguientes ingredientes para su receta: \n{receta1[0]}\n{receta1[1]}\n{receta1[2]}")
    else:
        print("la opción ingresada no es valida, ejecute nuevamente el programa.")
elif tipo_receta==2:
    print("Usted eligio la receta ", tipo_receta)
    print(f"Sus opciones son: \n1:{receta2[0]} \n2:{receta2[1]} \n3:{receta2[2]} \n4:{receta2[3]}")
    ingrediente_a_eliminar= int(input("Seleccione el ingrediente que no desea usar:\n"))-1
    if receta2.len>=ingrediente_a_eliminar:
        receta2.remove(receta2[ingrediente_a_eliminar])
        print(f"Usted eligio los siguientes ingredientes para su receta: \n{receta2[0]}\n{receta2[1]}\n{receta2[2]}")
    else:
        print("la opción ingresada no es valida, ejecute nuevamente el programa.")
else:
    print("El numero de receta elegido es incorrecto, debe ejecutar el programa nuevamente.")

#Opcion 2

""" recetaElegida=[]

if tipo_receta==1:
    print("Usted eligio la receta ", tipo_receta)
    print(f"Opciones: \n1:{receta1[0]} \n2:{receta1[1]} \n3:{receta1[2]} \n4:{receta1[3]}")
    ingrediente1=int(input("Seleccione el primer ingrediente:\n"))-1
    print(len(receta1))
    if len(receta1)>ingrediente1:
        recetaElegida.append(receta1[ingrediente1])
        ingrediente2=int(input("Seleccione el segundo ingrediente:\n"))-1
        if len(receta1)>ingrediente2:
            recetaElegida.append(receta1[ingrediente2])
            ingrediente3=int(input("Seleccione el tercer ingrediente:\n"))-1
            if len(receta1)>ingrediente3:
                recetaElegida.append(receta1[ingrediente3])
                print(f"Usted eligio los siguientes ingredientes para su receta: \n{recetaElegida[0]}\n{recetaElegida[1]}\n{recetaElegida[2]}")
            else:
                print("la opcion ingresada no es valida, ejecute el programa nuevamente.")
        else:
            print("la opcion ingresada no es valida, ejecute el programa nuevamente.")
    else:
        print("la opcion ingresada no es valida, ejecute el programa nuevamente.")
elif tipo_receta==2:
    print("Usted eligio la receta ", tipo_receta)
    print(f"Sus opciones son: \n1:{receta2[0]} \n2:{receta2[1]} \n3:{receta2[2]} \n4:{receta2[3]}")
    ingrediente1=int(input("Seleccione el primer ingrediente:\n"))-1
    if len(receta2)>ingrediente1:
        recetaElegida.append(receta2[ingrediente1])
        ingrediente2=int(input("Seleccione el segundo ingrediente:\n"))-1
        if len(receta2)>ingrediente2:
            recetaElegida.append(receta2[ingrediente2])
            ingrediente3=int(input("Seleccione el tercer ingrediente:\n"))-1
            if len(receta2)>ingrediente3:
                recetaElegida.append(receta2[ingrediente3])
                print(f"Usted eligio los siguientes ingredientes para su receta: \n{recetaElegida[0]}\n{recetaElegida[1]}\n{recetaElegida[2]}")
            else:
                print("la opcion ingresada no es valida, ejecute el programa nuevamente.")
        else:
            print("la opcion ingresada no es valida, ejecute el programa nuevamente.")
    else:
        print("la opcion ingresada no es valida, ejecute el programa nuevamente.")
else:
    print("El numero de receta elegido es incorrecto, debe ejecutar el programa nuevamente") """