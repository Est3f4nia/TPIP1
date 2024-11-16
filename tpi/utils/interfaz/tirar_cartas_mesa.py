# Funciona, falta integrar con el programa

def mesa(manoj, ronda, jugador):
    carta = int(input("Seleccione una carta: "))
    carta -= 1

    if jugador == 1:
        ronda[1] = manoj[carta]
    elif jugador == 2:
        ronda[0] = manoj[carta]
    
    manoj.remove(manoj[carta])

    return manoj, ronda
