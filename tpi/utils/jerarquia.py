# Funciona

def comparar_cartas(vector):
    jerarquia_truco = {
            ('1','Espada') : 13,
            ('1','Basto'): 12,
            ('7','Espada'): 11,
            ('7','Oro'): 10,
            3: 9,
            2: 8,
            ('1','Copa'): 7,
            ('1','Oro'): 7,
            12: 6,
            11: 5,
            10: 4,
            ('7','Copa'): 3,
            ('7','Basto'): 3,
            6: 2,
            5: 1,
            4: 0
        }

    if vector[0][0] == '1' or vector[0][0] == '7':
        valor_1 = jerarquia_truco[vector[0][0], vector[0][1]]
    elif vector[0][0]:
        valor_1 = jerarquia_truco[vector[0][0]]
        print(valor_1)

    if vector[1][0] == '1' or vector[1][0] == '7':
        valor_2 = jerarquia_truco[vector[1][0], vector[1][1]]
    else:
        valor_2 = jerarquia_truco[vector[1][0]]
        print(valor_2)
        
    # Fijate el tema de los retornos, podes modificar lo que retorne la función
    if valor_1 > valor_2:
        return vector[0]
    elif valor_2 > valor_1:
        return vector[1]
    elif valor_1 == valor_2:    
        return True
