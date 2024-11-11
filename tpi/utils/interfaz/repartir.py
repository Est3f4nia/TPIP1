# Maravilla de la programación

import random
def repartir():
    PALO = ['Espada', 'Oro', 'Basto', 'Copas']
    VALOR = ['1', '2', '3', '4', '5', '6', '7', '11', '12']
    mazo_jugador1 = [0] * 3
    mazo_jugador2 = [0] * 3
    for i in range(3):
        p = random.choice(PALO)
        n = random.choice(VALOR)
        carta = n, p
        if carta not in mazo_jugador1:
            mazo_jugador1[i] = n, p
        else:
            p = random.choice(PALO)
            n = random.choice(VALOR)
            carta = n, p
    
        p2 = random.choice(PALO)
        n2 = random.choice(VALOR)
        carta2 = n2, p2
        if carta2 not in mazo_jugador1 and carta2 not in mazo_jugador2:
            mazo_jugador2[i] = n2, p2
        else:
            p2 = random.choice(PALO)
            n2 = random.choice(VALOR)
            mazo_jugador2[i] = n2, p2
    return mazo_jugador1, mazo_jugador2
