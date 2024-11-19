from utils import jerarquia


def mesa(manoj, ronda, jugador, punto_pacial1, punto_pacial2):
    carta = int(input("\nSeleccione una carta: "))
    carta -= 1

    if jugador == 1:
        ronda[1] = manoj[carta]
    elif jugador == 2:
        ronda[0] = manoj[carta]

    if ronda[0] != 0 and ronda[1] != 0:
        carta_alta = jerarquia.comparar_cartas(ronda)
        
        if carta_alta == ronda[1]:
            punto_pacial1 += 1
        elif carta_alta == ronda[0]:
            punto_pacial2 += 1
        elif carta_alta == True:
            punto_pacial1 += 1
            punto_pacial2 += 1
    
    manoj.pop(carta)

    return manoj, ronda, punto_pacial1, punto_pacial2
