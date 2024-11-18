def mostrar_menu_muebles():
    print("¿Qué tipo de mueble quieres?")
    print("Categorías de muebles:")
    print("1. Cocina.")
    print("   Tipos de muebles: mesa, silla, despensa, repisa.")
    print("2. Dormitorio.")
    print("   Tipos de muebles: cama, mesa de luz, ropero.")
    print("3. Living.")
    print("   Tipos de muebles: modular, sillón, sofá, mesa ratonera.")
    print("4. Baño.")
    print("   Tipos de muebles: repisa, botiquín.")
    print("5. Oficina.")
    print("   Tipos de muebles: escritorio, silla, repisa, cajonera.")

def mostrar_menu_madera():
    print("¿Qué tipo de madera?")
    print("A) Roble")
    print("B) Cerezo")
    print("C) Abedul")
    print("D) Pino")
    print("E) Cedrus")
    print("F) Nogal")
    print("G) Abeto")
    print("H) Olivo")

def obtener_medidas():
    longitud = float(input("Ingrese la longitud del mueble (cm): "))
    grosor = float(input("Ingrese el grosor del mueble (cm): "))
    altura = float(input("Ingrese la altura del mueble (cm): "))
    anchura = float(input("Ingrese la anchura del mueble (cm): "))
    return longitud, grosor, altura, anchura

def obtener_divisiones():
    while True:
        divisiones = int(input("¿Cuántas divisiones debe tener? (de 2 a 20): ")) 
        if 2 <= divisiones <= 20:
            break
        else:
            print("Por favor, ingrese un número entre 2 y 20.")

    puertas = int(input("¿Cuántas son puertas? (0 a {}): ".format(divisiones)))
    repisas = int(input("¿Cuántas son repisas? (0 a {}): ".format(divisiones - puertas)))
    cajones = int(input("¿Cuántos son cajones? (0 a {}): ".format(divisiones - puertas - repisas)))

    return divisiones, puertas, repisas, cajones

def mainCM():
    mostrar_menu_muebles()
    tipo_mueble = input("Seleccione el tipo de mueble: ")
    
    mostrar_menu_madera()
    tipo_madera = input("Seleccione el tipo de madera: ")

    print("Complete las medidas del mueble ya terminado:")
    medidas = obtener_medidas()

    divisiones, puertas, repisas, cajones = obtener_divisiones()

    print("\nResumen de la creación del mueble:")
    print("Tipo de mueble:", tipo_mueble)
    print("Tipo de madera:", tipo_madera)
    print("Medidas (longitud, grosor, altura, anchura):", medidas)
    print("Divisiones:", divisiones)
    print("Puertas:", puertas)
    print("Repisas:", repisas)
    print("Cajones:", cajones)
