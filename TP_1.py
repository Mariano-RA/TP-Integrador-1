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


def formato_enunciado(operacion, A, B, dificultad):
    """
    Formatea y muestra el enunciado de la operación binaria.

    Args:
        operacion: String con la operación a realizar ('AND', 'OR', 'XOR', etc.)
        A: Primer número binario (en formato string)
        B: Segundo número binario (en formato string)
        dificultad: Número de bits utilizados

    Returns:
        Un string con el enunciado formateado para mostrar al usuario
    """
    # Asegurar que los números tengan el formato correcto según la dificultad
    A = A.zfill(dificultad)
    B = B.zfill(dificultad)

    # Crear el enunciado según el tipo de operación
    enunciado = f"{A} {operacion} {B} --> ¿Cuál es el resultado en binario?"

    return enunciado

def ejecutar_juego(dificultad, cant_partidas):
    
    #Inicializa la posicion en 1 para el contador de partidas
    contador_partidas = 1

    print("Bienvenidos al desafio de Operaciones Binarias y Numeros Binarios!!!")
    print(f'Seleccionaste jugar con {dificultad} bits! Cada respuesta correcta avanzas 1 posición y cada incorrecta te hace retroceder, llega a la posición {cant_partidas} para ganar!!' )
    
    while contador_partidas < cant_partidas:

        # Llama a la funcion operacion_aleatoria y le pasa por parametro la dificultad para devolver el enunciado a mostrar por pantalla y la respuesta correcta.
        enunciado, resultado_correcto = operacion_aleatoria(dificultad)
        
        print(f'Posición: {contador_partidas}')
        print(enunciado)

        # Solicita la respuesta al usuario, se le hace strip si por accidente apreta un espacio. 
        # No hay validaciòn de datos porque si ingresa el numero incorrecto o una letra ya no es la respuesta correcta
        respuesta = input('Ingresa tu respuesta: ').strip()

        # Se comprueba la respuesta con el resultado correcto que viene de la funcion operacion aleatoria
        # Si es correcta, se suma uno al contador de partidas y vuelve a empezar, si es incorrecta resta al contador.
        if respuesta == resultado_correcto:
            contador_partidas += 1
            print(f'Excelente!! Respuesta correcta, avanzas una posición, quedan {cant_partidas - contador_partidas}')
        else:
            contador_partidas = max(1, contador_partidas - 1)
            print (f'Mala suerte! la respuesta correcta era: {resultado_correcto}. Retrocedes a la posicion {contador_partidas}. A meterle ganas pichón.')
    
    # Finalizado el juego saca un print notificando al usuario y felicitandolo.
    print(f'Felicitaciones!!! Lograste completar el desafio!! Hasta el próximo trabajo práctico!')



if __name__ == "__main__":
    dificultad, cant_partidas = seleccion_dificultad()
    ejecutar_juego(dificultad, cant_partidas)