import os

from tpi.utils.interfaz import (opciones_usuario, presentacion_mano, repartir, mostrar_cartas_mesa)

mano1 = [0] * 2
mano2 = [0] * 2
mano3 = [0] * 2

jugador = 1
ronda = 0
puntosj1 = 0
puntosj2 = 0

reiniciar = False
manoj1, manoj2 = repartir.repartir()
valor_mano = 1

ultimo_en_cantar = 0

punto_pacial1 = 0
punto_pacial2 = 0

def mainT(mano1, mano2, mano3, jugador, ronda, puntosj1, puntosj2, reiniciar, manoj1, manoj2, valor_mano, ultimo_en_cantar, punto_pacial1, punto_pacial2):
    while reiniciar == False:
        os.system("cls")
        print("----- Truco en consola -----")
        print("Turno del jugador", jugador)
        print("Puntos:", puntosj1, "-", puntosj2)
        print("Valor de la mano:", valor_mano)

        mostrar_cartas_mesa.mostrar_cartas_mesa(mano1, mano2, mano3, ronda, punto_pacial1, punto_pacial2)

        if jugador == 1:
            if ronda == 0:
                presentacion_mano.mostrar_mano(jugador, manoj1)
                reiniciar, repetir, valor_mano, punto_pacial1, punto_pacial2, ultimo_en_cantar = opciones_usuario.opciones_jugador(ronda, jugador, manoj1, manoj2, mano1, reiniciar, valor_mano, punto_pacial1, punto_pacial2, ultimo_en_cantar)
            elif ronda == 1:
                presentacion_mano.mostrar_mano(jugador, manoj1)
                reiniciar, repetir, valor_mano, punto_pacial1, punto_pacial2, ultimo_en_cantar = opciones_usuario.opciones_jugador(ronda, jugador, manoj1, manoj2, mano2, reiniciar, valor_mano, punto_pacial1, punto_pacial2, ultimo_en_cantar)
            elif ronda == 2:
                presentacion_mano.mostrar_mano(jugador, manoj1)
                reiniciar, repetir, valor_mano, punto_pacial1, punto_pacial2, ultimo_en_cantar = opciones_usuario.opciones_jugador(ronda, jugador, manoj1, manoj2, mano3, reiniciar, valor_mano, punto_pacial1, punto_pacial2, ultimo_en_cantar)
        
        if jugador == 2:
            if ronda == 0:
                presentacion_mano.mostrar_mano(jugador, manoj2)
                reiniciar, repetir, valor_mano, punto_pacial1, punto_pacial2, ultimo_en_cantar = opciones_usuario.opciones_jugador(ronda, jugador, manoj1, manoj2, mano1, reiniciar, valor_mano, punto_pacial1, punto_pacial2, ultimo_en_cantar)
                if mano1[0] != 0 and mano1[1] != 0:
                    ronda += 1
            elif ronda == 1:
                presentacion_mano.mostrar_mano(jugador, manoj2)
                reiniciar, repetir, valor_mano, punto_pacial1, punto_pacial2, ultimo_en_cantar = opciones_usuario.opciones_jugador(ronda, jugador, manoj1, manoj2, mano2, reiniciar, valor_mano, punto_pacial1, punto_pacial2, ultimo_en_cantar)
                if mano2[0] != 0 and mano2[1] != 0:
                    ronda += 1
            elif ronda == 2:
                presentacion_mano.mostrar_mano(jugador, manoj2)
                reiniciar, repetir, valor_mano, punto_pacial1, punto_pacial2, ultimo_en_cantar = opciones_usuario.opciones_jugador(ronda, jugador, manoj1, manoj2, mano3, reiniciar, valor_mano, punto_pacial1, punto_pacial2, ultimo_en_cantar)
                if mano3[0] != 0 and mano3[1] != 0:
                    ronda += 1

        if repetir == False:
            if jugador == 1:
                jugador = 2
            elif jugador == 2:
                jugador = 1
            os.system("cls")
            
        # ver si terminó
        if ronda == 4 or punto_pacial1 == 2 or punto_pacial2 == 2:
            reiniciar = True
        
        if reiniciar == True:
            print("----- Fin de la mano -----")
            
            # dar puntos
            if punto_pacial1 == 2:
                print("El jugador 1 ganó", valor_mano, "puntos")
                puntosj1 += valor_mano
                jugador = 1
            else:
                print("El jugador 2 ganó", valor_mano, "puntos")
                puntosj2 += valor_mano
                jugador = 2

            print("Repartiendo...")
            mano1 = [0] * 2
            mano2 = [0] * 2
            mano3 = [0] * 2

            ronda = 0
            manoj1, manoj2 = repartir.repartir()
            valor_mano = 1
            punto_pacial1 = 0
            punto_pacial2 = 0
            reiniciar = False
            
            if puntosj1 >= 15 or puntosj2 >= 15:
                reiniciar = True
            
            input("Presione enter para continuar")
        else:
            print("Cambio de jugador...")
            input("Presione enter para continuar")

    print("----- Fin del juego -----")
    print("Puntos:", puntosj1, "-", puntosj2)
