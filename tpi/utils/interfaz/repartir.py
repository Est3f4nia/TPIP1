# Maravilla de la programación

import random


def repartir():
    PALO = ['Espada', 'Oro', 'Basto', 'Copa']
    VALOR = ['1', 2, 3, 4, 5, 6, '7', 10, 11, 12]
    mazo_jugador1 = [0] * 3
    mazo_jugador2 = [0] * 3
    for i in range(6):
        while True:
            p = random.choice(PALO)
            n = random.choice(VALOR)
            carta = n, p
            if carta not in mazo_jugador1 and carta not in mazo_jugador2:
                break
        if i < 3:
            mazo_jugador1[i] = n, p
        else:
            mazo_jugador2[i-3] = n, p
    return mazo_jugador1, mazo_jugador2
