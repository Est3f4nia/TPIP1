from buscaminas import (jugar)
from programa import (mainCM)
from tpi.mainT import (mainT)

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
        tpi.mainT.mainT()
    else:
        print("Opción inválida")
