def seleccion_dificultad():
    while True:
        try:
            dificultad = int(input("Elige la dificultad (número de bits: 4, 5 o 6): "))
            if dificultad in [4, 5, 6]:
                break
            else:
                print("Por favor, elige 4, 5 o 6.")
        except ValueError:
            print("Entrada no válida. Ingresa un número.")

    while True:
        try:
            cant_partidas = int(input("¿Cuántas partidas quieres jugar?: "))
            if cant_partidas > 0:
                break
            else:
                print("El número de partidas debe ser mayor que 0.")
        except ValueError:
            print("Entrada no válida. Ingresa un número.")

    return dificultad, cant_partidas

seleccion_dificultad()