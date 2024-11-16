def cambiar_ronda(mazo,canto, ronda3, reiniciar):
    if mazo == True:
        reiniciar = True

    if canto == "nq":
        reiniciar = True
    
    if ronda3[0] != 0 and ronda3[1] != 0:
        reiniciar = True
    return reiniciar
