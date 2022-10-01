import random

victorias_jugador = 0
victorias_pc=0 
ganador= ""
tirada=1

def lanzar_dado():
    tirada= random.randint(1,6)
    return tirada

print("que comience el juego!\n(Gana el mejor de 3)")

""" def jugar(): """
while (victorias_jugador < 3 and victorias_pc < 3):
    print(f"tirada {tirada}:")
    tirada+=1
    jugador= lanzar_dado()
    pc= lanzar_dado()
    """ if(xor(jugador,pc)): """
    if(pc==jugador):
        print("Empate")
    elif(jugador>pc):
        victorias_jugador +=1
        print("ganó jugador")
    else:
        victorias_pc +=1
        print("ganó pc")

if (victorias_jugador>victorias_pc):
    ganador = "jugador"
else:
    ganador = "pc"

print (f"Juego finalizado:\njugador ganó: {victorias_jugador} veces \npc ganó: {victorias_pc} veces")
print (f"El ganador es: {ganador}")