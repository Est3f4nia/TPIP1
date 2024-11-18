from buscaminas import (jugar)
from programa import (mainCM)
from tpi.mainT import (mainT)
from tpi.utils.interfaz.repartir import (repartir)

print("----- TPI Grupo 5 -----")
print('1) Buscaminas')
print('2) Creador de muebles')
print('3) Truco')
opcion = int(input('Seleccione una opción: '))

while opcion != 0:
    if opcion == 1:
        buscaminas.jugar()
    elif opcion == 2:
        programa.mainCM()
    elif opcion == 3:
        mano1 = [0] * 2
        mano2 = [0] * 2
        mano3 = [0] * 2
        jugador = 1
        ronda = 0
        puntosj1 = 0
        puntosj2 = 0
        reiniciar = False
        manoj1, manoj2 = tpi.utils.interfaz.repartir.repartir()
        valor_mano = 1
        ultimo_en_cantar = 0
        punto_pacial1 = 0
        punto_pacial2 = 0

        tpi.mainT.mainT(mano1, mano2, mano3, jugador, ronda, puntosj1, puntosj2, reiniciar, manoj1, manoj2, valor_mano, ultimo_en_cantar, punto_pacial1, punto_pacial2)
    else:
        print("Opción inválida")
