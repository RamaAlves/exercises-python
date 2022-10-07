""" Para seguir colaborando en esta misión de salvar al planeta, necesitamos que elabores un 
programa en Python que dado el tamaño de un pez indique si su organismo está contaminado. Para ello tendremos 4 opciones:
Tamaño Normal: Mensaje "Pez en buenas condiciones"
Tamaño por debajo de lo Normal: Mensaje "Pez con problemas de nutrición"
Tamaño un poco por encima de lo Normal: Mensaje "Pez con síntomas de organismo contaminado"
Tamaño sobredimensionado: Mensaje "Pez contaminado" """

tamañoPez = float(input("ingrese el tamaño del pez en cm:\n"))

if tamañoPez<9:
    print("Pez con problemas de nutrición")
elif tamañoPez>=9 and tamañoPez<=12:
    print("Pez en buenas condiciones")
elif tamañoPez>12 and tamañoPez<=15:
    print("Pez con síntomas de organismo contaminado")
else:
    print("Pez contaminado")