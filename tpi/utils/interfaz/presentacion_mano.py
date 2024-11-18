# Completo

def mostrar_mano(jugador, mano):
    for i in range(len(mano)):
            print(i + 1, ") ", mano[i][0], " de ", mano[i][1], sep = "")
