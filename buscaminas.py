import random

def crear_tablero(tamaño, num_minas):
    tablero = [[0 for i in range(tamaño)] for j in range(tamaño)]
    minas_colocadas = 0

    while minas_colocadas < num_minas:
        fila = random.randint(0, tamaño - 1)
        columna = random.randint(0, tamaño - 1)
        if tablero[fila][columna] != "💣":  
            tablero[fila][columna] = "💣"
            minas_colocadas += 1

            for i in range(max(0, fila - 1), min(tamaño, fila + 2)):
                for j in range(max(0, columna - 1), min(tamaño, columna + 2)):
                    if tablero[i][j] != "💣":
                        tablero[i][j] += 1
    return tablero

def mostrar_tablero(tablero, revelado):
    tamaño = len(tablero)
    print("  " + " ".join(str(i + 1) for i in range(tamaño)))  
    for i in range(tamaño):
        fila = []
        for j in range(tamaño):
            if revelado[i][j]:
                fila.append(str(tablero[i][j]))
            else:
                fila.append("□")
        print(str(i + 1) + " " + " ".join(fila))  

def descubrir(tablero, revelado, fila, columna):
    fila -= 1  
    columna -= 1  
    if revelado[fila][columna]:
        return
    revelado[fila][columna] = True

    if tablero[fila][columna] == "💣":  
        return True
    elif tablero[fila][columna] == 0:
        tamaño = len(tablero)
        for i in range(max(0, fila - 1), min(tamaño, fila + 2)):
            for j in range(max(0, columna - 1), min(tamaño, columna + 2)):
                if not revelado[i][j]:
                    descubrir(tablero, revelado, i + 1, j + 1)  
    return False

def jugar():
    tamaño = int(input("Ingrese el tamaño del tablero: "))
    num_minas = int(input("Ingrese el número de minas: "))
    
    tablero = crear_tablero(tamaño, num_minas)
    revelado = [[False for _ in range(tamaño)] for _ in range(tamaño)]
    terminado = False

    while not terminado:
        mostrar_tablero(tablero, revelado)
        fila = int(input("Ingrese la fila (1 a {}): ".format(tamaño)))
        columna = int(input("Ingrese la columna (1 a {}): ".format(tamaño)))

        if descubrir(tablero, revelado, fila, columna):
            print("¡Boom! Perdiste.")
            terminado = True
        else:
            celdas_restantes = sum(not revelado[i][j] for i in range(tamaño) for j in range(tamaño) if tablero[i][j] != "💣")
            if celdas_restantes == 0:
                print("¡Felicitaciones! Ganaste.")
                terminado = True

    mostrar_tablero(tablero, [[True for _ in range(tamaño)] for _ in range(tamaño)])

jugar()
