# Incompleto

def jerarquia(matriz_mesa, ronda):
    for carta in matriz_mesa[ronda]:
        jerarquia_truco = {
            ('1','Espada') : 13,
            ('1','Basto'): 12,
            ('7','Espada'): 11,
            ('7','Oro'): 10,
            '3': 9,
            '2': 8,
            ('1','Copa'): 7,
            ('1','Oro'): 7,
            '12': 6,
            '11': 5,
            '10': 4,
            ('7','Copa'): 3,
            ('7','Basto'): 3,
            '6': 2,
            '5': 1,
            '4': 0
        }
