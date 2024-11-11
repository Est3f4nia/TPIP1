# Incompleto

import os
from utils.interfaz.presentacion_mano import (mostrar_mano)

def truco(ronda, jugador, mano, valor_mano, reiniciar):
    if ronda:
        os.system("cls")
        aux = input("Presione cualquier tecla para continuar")
        print("Turno del jugador", jugador)
        mostrar_mano(jugador, mano)
        print("\nSe cantó truco")
        canto = input('¿Se quiere? ("q" o "nq"): ')
        if canto == "q":
            valor_mano = valor_mano + 1
            os.system("cls")
        elif canto == "nq":
            os.system("cls")
            reiniciar = True
    return valor_mano, reiniciar
