import random

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
        operacion: String con la operación a realizar ('AND', 'OR', 'XOR', 'NOT', etc.)
        A: Primer número binario (en formato string)
        B: Segundo número binario (en formato string) - No usado para NOT
        dificultad: Número de bits utilizados
    
    Returns:
        Un string con el enunciado formateado para mostrar al usuario
    """
    # Caso especial para NOT (operación unaria)
    if operacion == "NOT":
        # Para NOT, solo utilizamos A con el formato correcto
        A = A.zfill(dificultad)
        enunciado = f"{operacion} {A} --> ¿Cuál es el resultado en binario?"
    else:
        # Para operaciones binarias, utilizamos ambos valores con formato correcto
        A = A.zfill(dificultad)
        B = B.zfill(dificultad)
        enunciado = f"{A} {operacion} {B} --> ¿Cuál es el resultado en binario?"
    
    return enunciado

def operacion_aleatoria(dificultad):
    """
    Genera una operación lógica binaria aleatoria entre dos números binarios
    y muestra el enunciado correspondiente al usuario.

    La operación seleccionada será una de las siguientes: 'AND', 'OR', 'XOR', 'NOT'.
    Los números binarios generados tienen una longitud determinada por el parámetro 'dificultad'.
    Dependiendo de la operación y el resultado se calcula y se muestra al usuario como un enunciado.
    """
    
    bin1 = format(random.randint(0, 2**dificultad - 1), f'0{dificultad}b') 
    bin2 = format(random.randint(0, 2**dificultad - 1), f'0{dificultad}b') 

    compuerta = random.choice(["AND","OR","XOR","NOT"])

    a_int = int(bin1, 2)
    b_int = int(bin2, 2)
    
    if compuerta == 'AND':
        resultado_correcto = format(a_int & b_int, f'0{len(bin1)}b')
    elif compuerta == 'OR':
        resultado_correcto = format(a_int | b_int, f'0{len(bin1)}b')
    elif compuerta == 'XOR':
        resultado_correcto = format(a_int ^ b_int, f'0{len(bin1)}b')
    elif compuerta == 'NOT':
        resultado_correcto = format(~a_int & (2**len(bin1)-1), f'0{len(bin1)}b')

    return formato_enunciado(compuerta, bin1, bin2, dificultad), resultado_correcto

def mostrar_progreso(contador_partidas, cant_partidas):
    
    #Funcion que formatea la posicion del jugador y la cantidad de partidas restantes

    print(f'Posición: {contador_partidas}')
    print(f'Necesitas {cant_partidas - contador_partidas} partidas para ganar!!\n')

def preguntar_finalizar(contador_partidas_perdidas, dificultad):

    # Se reciben la cantidad de partidas perdidas y la dificultad, con esos datos se define la cantidad de errores tolerados

    if dificultad == 4:
        errores_tolerados = 3
    elif dificultad == 5:
        errores_tolerados = 4
    else:
        errores_tolerados = 5

    if contador_partidas_perdidas >= errores_tolerados:

        #Si vemos que el contador de partidas perdidas es mayor o igual a los errores tolerados le vamos a consultar al usuario si le gustaria continuar o no

        respuesta = input("\nParece que estás teniendo dificultades... ¿Querés terminar el juego? (s/n): ").strip().lower()
        while respuesta != 's' and respuesta != 'n':
            respuesta = input("Por favor responde 's' (sí) o 'n' (no): ").strip().lower()
        return respuesta == 's'
    return False

def ejecutar_juego():
    
    #Inicializa la posicion en 1 para el contador de partidas
    contador_partidas = 1
    contador_partidas_perdidas = 0

    print("-------------------------------------------------------------------------------------")
    print("Bienvenidos al desafio de Operaciones Booleanas y Numeros Binarios!!!")
    print("-------------------------------------------------------------------------------------")

    dificultad, cant_partidas = seleccion_dificultad()

    print(f'\n\nSeleccionaste jugar con {dificultad} bits! Cada respuesta correcta avanzas 1 posición y cada incorrecta te hace retroceder, llega a la posición {cant_partidas} para ganar!!\n' )
    
    while contador_partidas < cant_partidas:

        # Llama a la funcion operacion_aleatoria y le pasa por parametro la dificultad para devolver el enunciado a mostrar por pantalla y la respuesta correcta.
        enunciado, resultado_correcto = operacion_aleatoria(dificultad)
        
        mostrar_progreso(contador_partidas, cant_partidas)

        print(enunciado)

        # Solicita la respuesta al usuario, se le hace strip si por accidente apreta un espacio. 
        # No hay validaciòn de datos porque si ingresa el numero incorrecto o una letra ya no es la respuesta correcta
        respuesta = input('Ingresa tu respuesta: ').strip()

        # Se comprueba la respuesta con el resultado correcto que viene de la funcion operacion aleatoria
        # Si es correcta, se suma uno al contador de partidas y vuelve a empezar, si es incorrecta resta al contador.
        if respuesta == resultado_correcto:
            contador_partidas += 1
            print(f'\nExcelente!! Respuesta correcta, avanzas una posición, quedan {cant_partidas - contador_partidas}')
        else:
            contador_partidas = max(1, contador_partidas - 1)
            print (f'Mala suerte! la respuesta correcta era: {resultado_correcto}. Retrocedes a la posicion {contador_partidas}. A meterle ganas pichón.')
            contador_partidas_perdidas += 1

            # Verificar si quiere finalizar
            if preguntar_finalizar(contador_partidas_perdidas, dificultad):
                print("No pasa nada, la próxima te va a ir mejor!! Juego finalizado.")
                return
    
    # Finalizado el juego saca un print notificando al usuario y felicitandolo.
    print(f'Felicitaciones!!! Lograste completar el desafio!! Hasta el próximo trabajo práctico!')

if __name__ == "__main__":
    ejecutar_juego()