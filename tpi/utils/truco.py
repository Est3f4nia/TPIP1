import os
from utils.interfaz import presentacion_mano


def truco(ronda, jugador, mano, valor_mano, reiniciar, ultimo_en_cantar):
    os.system("cls")
    print("Cambio de jugador")
    input("Presione enter para continuar")
    print("Turno del jugador", jugador)
    presentacion_mano.mostrar_mano(jugador, mano)
    print("\nSe cantó el petiso")
    if valor_mano == 1:
        print("Se cantó: Truco")
    elif valor_mano == 2:
        print("Se cantó: Retruco")
    elif valor_mano == 3:
        print("Se cantó: Vale Cuatro")
    canto = input('¿Se quiere? ("q" o "nq"): ')

    if canto == "q":
        valor_mano = valor_mano + 1
        os.system("cls")
        
    elif canto == "nq":
        os.system("cls")
        reiniciar = True
             
    return valor_mano, reiniciar, ultimo_en_cantar
