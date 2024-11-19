def mostrar_cartas_mesa(mano1, mano2, mano3, ronda, punto_pacial1, punto_pacial2):
    print("----- Cartas en la mesa -----")
    print("Cartas J1 - Cartas J2")
    if ronda >= 0:
        print("Mano 1:", obtener_carta(mano1[1]), "-", obtener_carta(mano1[0]))
    if ronda >= 1:
        print("Mano 2:", obtener_carta(mano2[1]), "-", obtener_carta(mano2[0]))
    if ronda >= 2:
        print("Mano 3:", obtener_carta(mano3[1]), "-", obtener_carta(mano3[0]))
    
    print("Puntos parciales de la mano:", punto_pacial1, "-", punto_pacial2)

def obtener_carta(carta):
    if carta == 0:
        return "Sin tirar"
    else:
        return carta
