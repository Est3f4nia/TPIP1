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

truco = 2

def truco (jugador1, jugador2):
    truco = 2
    truco = True
    if jugador1 >= jugador2:
        jugador1 += truco
        return jugador1, truco
    elif jugador2 >= jugador1:
        jugador2 += truco
        return jugador2, truco


trucont = 1
def trucont (jugador1,jugador2):
    trucont = 1
    truco = False
    if jugador1 == trucont:
        jugador2 += 1
        return jugador1, truco
    elif jugador2 == trucont:
        jugador1 += 1
        return jugador2, truco

retruco = 3

def retruco (jugador1,jugador2):
    if jugador1 >= jugador2:
        jugador1 += retruco
        return jugador1
    elif jugador2 >= jugador1:
        jugador2 += retruco
        return jugador2

retrucont = 2

def retrucont (jugador1,jugador2):
    if jugador1 == retrucont:
        jugador2 += 2
        return jugador1
    elif jugador2 == retrucont:
        jugador1 += 2
        return jugador2

vale_cuatro = 4

def vale_cuatro (jugador1,jugador2):
    if jugador1 >= jugador2:
        jugador1 += vale_cuatro
        return jugador1
    elif jugador2 >= jugador1:
        jugador2 += vale_cuatro
        return jugador2

vale_cuatront = 3

def vale_cuatront (jugador1,jugador2):
    if jugador1 == vale_cuatront:
        jugador2 += 3
        return jugador1
    elif jugador2 == vale_cuatront:
        jugador1 += 3
        return jugador2
