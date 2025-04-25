def seleccion_dificultad():
    
    # Se selecciona la cantidad de bits dentro de las opciones disponibles (4, 5 o 6) y se lo coloca dentro de un while true para manejar los errores si no responde correctamente
    while True:
        try:
            dificultad = int(input("Elige la dificultad (número de bits: 4, 5 o 6): "))
            if dificultad in [4, 5, 6]:
                break
            else:
                print("Por favor, elige 4, 5 o 6.")
        except ValueError:
            print("Entrada no válida. Ingresa un número.")

    
    # Se selecciona cuantas partidas desea jugar el usuario limitando que sean entre 1 y 10 igualmente con un while true para que si no responde correctamente se vuelva a ejecutar
    while True:
        try:
            cant_partidas = int(input("¿Cuántas partidas quieres jugar? (pueden ser como máximo 10): "))
            if cant_partidas > 0 and cant_partidas <= 10:
                break
            else:
                print("El número de partidas debe ser mayor que 0.")
        except ValueError:
            print("Entrada no válida. Ingresa un número.")

    
    # Se retornan los valores de dificultad y cantidad de partidas que el usuario selecciono
    return dificultad, cant_partidas
