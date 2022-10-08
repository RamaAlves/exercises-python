""" En un Centro Asistencial existen tres áreas: Pediatría, Traumatología y Kinesiología. El presupuesto anual del hospital se reparte conforme a la sig. tabla:
ÁREA 		        PORCENTAJE
Pediatría			60%
Traumatología  	    20%
Kinesiología		20%

Obtener la cantidad de dinero que recibirá cada área, para cualquier monto presupuestal 		que se ingrese por teclado. """

presupuestoAnual=float(input("Ingrese el presupuesto anual:\t$ "))

if presupuestoAnual>0:
    presupuestoPediatria=presupuestoAnual*0.6
    presupuestoTraumato=presupuestoAnual*0.2
    presupuestoKinesio=presupuestoAnual*0.2
    print(f"Con un presupuesto anual de ${presupuestoAnual} corresponde:\n\t${presupuestoPediatria} a pediatría.\n\t${presupuestoTraumato} a traumatología\n\t${presupuestoKinesio} a kinesiología")
else:
    print("El monto ingresado es muy bajo.")