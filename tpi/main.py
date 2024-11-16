# Incompleto

import random
from utils.interfaz.repartir import (repartir)
from utils.interfaz.presentacion_mano import (mostrar_mano)
from utils.interfaz.opciones_usuario import (opciones_jugador)

mano1 = [0] * 2
mano2 = [0] * 2
mano3 = [0] * 2

manoj1, manoj2 = repartir()

valor_ronda = 1
jugador = 1

puntosj1 = 0
puntosj2 = 0

reiniciar = False # Hay demasiadas funciones, ¿cómo podemos hacer llegar el valor True hasta acá?

while reiniciar == False:
    print("----- Truco en consola -----")
    print("Turno del jugador", jugador)
    print("Valor de la mano:", valor_ronda)

    if jugador == 1:
        print("Puntos:", puntosj1) # Incompleto
        mostrar_mano(jugador, manoj1)
        opciones_jugador(ronda, jugador, manoj1, manoj2, valor_ronda, reiniciar)
        jugador = 2
    if jugador == 2:
        print("Puntos:", puntosj2)
        mostrar_mano(jugador, manoj2)
        opciones_jugador(ronda, jugador, manoj2, valor_ronda, reiniciar)
        jugador = 1

    ronda += 1 # Idea para cambiar de ronda (repartir de nuevo)

if reiniciar == True: # Intento de reinicio
    manoj1, manoj2 = repartir()
    mano1 = [0] * 2
    mano2 = [0] * 2
    mano3 = [0] * 2

    reiniciar = False
