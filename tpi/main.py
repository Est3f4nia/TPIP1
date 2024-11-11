# Función truco: no incrementa el valor de la mano y al no querer no se reparten de nuevo las cartas
# Incompleto

import random
from utils.interfaz.repartir import (repartir)
from utils.interfaz.presentacion_mano import (mostrar_mano)
from utils.interfaz.opciones_usuario import (opciones_jugador)

mesaj1 = [[0 for i in range(1)] for j in range(3)]
mesaj2 = [[0 for i in range(1)] for j in range(3)]

manoj1, manoj2 = repartir()

ronda = 1
valor_mano = 1
jugador = 1

puntosj1 = 0
puntosj2 = 0

reiniciar = False

while ronda <= 3 or reiniciar == False:
    print("----- Truco en consola -----")
    print("Turno del jugador", jugador)
    print("Valor de la mano:", valor_mano)

    if jugador == 1:
        print("Puntos:", puntosj1)
        mostrar_mano(jugador, manoj1)
        opciones_jugador(ronda, jugador, manoj1, manoj2, valor_mano, reiniciar)
    if jugador == 2:
        print("Puntos:", puntosj2)
        mostrar_mano(jugador, manoj2)
        opciones_jugador(ronda, jugador, manoj2, valor_mano, reiniciar)

    ronda += 1

if reiniciar == True:
    manoj1, manoj2 = repartir()
    reiniciar = False
