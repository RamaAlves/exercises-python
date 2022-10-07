""" Se está desarrollando un sistema de control de vehículos desde donde se han tirado restos de basura a la vía pública.
Para ello la ciudad cuenta con sistemas de monitoreo de patentes que devuelve 3 letras y un valor numérico de 5 dígitos a 
la Central con el siguiente significado:
3 letras: Correspondientes a la patente.
Del valor numérico:
Los 3 primeros números corresponden a la patente
El 4 número indica
1- Tiró basura a la vía pública
0 - No tiró basura a la vía pública
El 5 número indica
1- Ya había sido multado el vehículo
0 - Vehículo sin multas.
Deberás informar cantidad de vehículos observados, cantidad de vehículos que han tirado basura y porcentaje de éstos que ya habían sido multados.

 """

vehiculos=0
ingresarVehiculo= True

vehiculosSucios=0
vehiculosSuciosYMultados=0

while ingresarVehiculo:
    codigo= str(input("ingrese el codigo recibido:\t"))
    vehiculos+=1
    if codigo[6]=="1":
        vehiculosSucios+=1
        if codigo[7]=="1":
            vehiculosSuciosYMultados+=1
    continuar=input("Desea ingresar mas vehiculos\ty/n\n")
    if continuar=="n":
        ingresarVehiculo=False

print("Mostrando stadisticas")
print("total de vehículos observados", vehiculos)
print("total de vehiculos que tiraron basura:\t", vehiculosSucios)
if vehiculosSucios:
    print(f"porcentaje de vehiculos que tiraron basura que tenian multas previas: \t{vehiculosSuciosYMultados*100/vehiculosSucios}%")