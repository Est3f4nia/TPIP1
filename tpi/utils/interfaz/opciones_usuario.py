from utils.interfaz import tirar_cartas_mesa
from utils.truco import truco

def opciones_jugador(ronda, jugador, mano1, mano2, mano_mesa, reiniciar, valor_mano, punto_pacial1, punto_pacial2, ultimo_en_cantar):
    repetir = False
    print("\n----- Opciones -----")
    if valor_mano == 1:
        print("1) Truco")
    if valor_mano == 2 and jugador != ultimo_en_cantar:
        print("1) Retruco")
    if valor_mano == 3 and jugador != ultimo_en_cantar:
        print("1) Vale Cuatro")

    print("2) Tirar carta")
    print("3) Mazo")
    opcion = int(input("Seleccione una opción: "))
    if jugador == 1:
        mano = mano1
    if jugador == 2:
        mano = mano2

    if opcion == 1:
        repetir = True
        if valor_mano != 4:
            
            if jugador == 1 and ultimo_en_cantar != 1:
                ultimo_en_cantar = 1
                valor_mano, reiniciar = truco(ronda, 2, mano2, valor_mano, reiniciar)
            elif jugador == 2 and ultimo_en_cantar != 2:
                valor_mano, reiniciar = truco(ronda, 1, mano1, valor_mano, reiniciar)
                ultimo_en_cantar = 2
            else:
                print("Ya lo cantaste.")

            if reiniciar:
                if jugador == 1:
                    punto_pacial1 = 2
                    punto_pacial2 = 0
                elif jugador == 2:
                    punto_pacial1 = 0
                    punto_pacial2 = 2
        else:
            print("No se puede cantar más.")
    
    elif opcion == 2:
        mano, mano_mesa, punto_pacial1, punto_pacial2 = tirar_cartas_mesa.mesa(mano, mano_mesa, jugador, punto_pacial1, punto_pacial2)

    elif opcion == 3:
        if jugador == 1:
            punto_pacial1 = 0
            punto_pacial2 = 2
        elif jugador == 2:
            punto_pacial1 = 2
            punto_pacial2 = 0
    else:
        print("Opción inválida.")
    
    return reiniciar, repetir, valor_mano, punto_pacial1, punto_pacial2, ultimo_en_cantar
