import random

def obtener_carta():
    cartas_validas = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
    return random.choice(cartas_validas)

def valor_carta(carta):
    if carta in [10, 11, 12]:
        return 0.5
    else:
        return carta

def turno_jugador(nombre):
    print(f"\nTurno de {nombre}:")
    puntuacion = 0
    while True:
        respuesta = input("¿Quieres carta? (si/no): ").lower()
        if respuesta == "si":
            carta = obtener_carta()
            valor = valor_carta(carta)
            puntuacion += valor
            print(f"Tu carta es: {carta}")
            print(f"Acumulas: {puntuacion}")
            
            if puntuacion == 7.5:
                print("¡Has ganado! Llegaste al 7.5.")
                break
            elif puntuacion > 7.5:
                print("Te has pasado de 7.5.")
                break
        elif respuesta == "no":
            print(f"Te has plantado con {puntuacion} puntos.")
            break
        else:
            print("Introduce si o no.")
    
    return puntuacion

def turno_banca():
    print("\nTurno de la Banca:")
    puntuacion = 0
    while puntuacion < 5.5 or (puntuacion >= 5.5 and puntuacion <= 7.5):
        carta = obtener_carta()
        valor = valor_carta(carta)
        puntuacion += valor
        print(f"La banca saca la carta: {carta}")
        print(f"La banca acumula: {puntuacion}")
        
        if puntuacion >= 7.5:
            break
    
    return puntuacion

def determinar_ganador(puntuacion_jugador, puntuacion_banca, nombre):
    print(f"\n{nombre} ha conseguido {puntuacion_jugador} puntos.")
    print(f"La banca ha conseguido {puntuacion_banca} puntos.")

    if puntuacion_jugador > 7.5 and puntuacion_banca > 7.5:
        print("Perdisteis los dos, pasasteis de 7.5.")
    elif puntuacion_jugador > 7.5:
        print("Te has pasado de 7.5. ¡Gana la banca!")
    elif puntuacion_banca > 7.5:
        print("La banca se ha pasado de 7.5. ¡Ganas tú!")
    elif puntuacion_jugador == 7.5 and puntuacion_banca < 7.5:
        print("¡Has ganado! Llegaste al 7.5.")
    elif puntuacion_banca == puntuacion_jugador:
        print("¡Empate!")
    elif puntuacion_banca >= 5.0 and puntuacion_banca <= 7.5:
        if puntuacion_jugador < puntuacion_banca:
            print("La banca tiene más puntos. ¡Gana la banca!")
        else:
            print("Tienes más puntos que la banca. ¡Ganas tú!")
    else:
        print("¡Ganas tú!")

print("Bienvenido al juego del 7 y medio")
nombre = input("Introduce tu nombre: ")

while True:
    puntuacion_jugador = turno_jugador(nombre)
    puntuacion_banca = turno_banca()
    
    determinar_ganador(puntuacion_jugador, puntuacion_banca, nombre)
    
    while True:
        respuesta = input("\n¿Quieres jugar otra partida? (si/no): ").lower()
        if respuesta == "si" or respuesta == "no":
            break
        else:
            print("Introduce si o no.")
    
    if respuesta != "si":
        print("Gracias por jugar. Finaliza la partida.")
        break
