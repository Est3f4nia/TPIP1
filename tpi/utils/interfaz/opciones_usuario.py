# incompleto

import os
from utils.cantos.truco import (truco)

def opciones_jugador(ronda, jugador, mano1, mano2, valor_mano, reiniciar):
    print("----- Opciones -----")
    print("1) Truco")
    print("2) Envido")
    print("3) Mazo")
    print("4) Tirar carta")
    opcion = int(input("Seleccione una opción: "))
    if opcion == 1:
        if jugador == 1:
            jugador += 1
            mano = mano2
        elif jugador == 2:
            jugador -= 1
            mano = mano1
        truco(ronda, jugador, mano, valor_mano, reiniciar)
    elif opcion == 2:
        pass

        
    elif opcion == 3:
        mazo()
    elif opcion == 4:
        mazo()
    else:
        print("Opción inválida.")
    return valor_mano
