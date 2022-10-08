""" Calcular el número de pulsaciones que una persona debe tener por cada 10 segundos de ejercicio, 
si la fórmula es: Número de pulsaciones = (220 - edad)/10 """

edad=int(input("Indique su edad:\t"))

if edad>0:
    pulsaciones=(220-edad)//10 #opte por utilizar division entera para que la lectura sea mas clara
    print("Al realizar ejercicio sus pulsaciones deberian ser de ",pulsaciones, " cada 10 segundos. Y de ", pulsaciones*6," por minuto.")
else:
    print("ingrese una edad valida")
