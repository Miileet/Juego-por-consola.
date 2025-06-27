from library import * 
from validaciones import *
from Historial import guardar_datos
import random

nombre = nombre_usuario()
seguir = desea_seguir_jugando()

while seguir == "s":
    print(f"Estas en el casillero {pos_jugador}")
    resultado = hacer_preguntas(nombre)
    pos_jugador = movimiento(pos_jugador, resultado)
    estado = verificar_estado_juego(pos_jugador, nombre, tablero)
    if estado != "continua":
        mostrar_tablero_con_jugador(tablero, pos_jugador)
        break
    print(f"Ahora estás en el casillero {pos_jugador}")
    mostrar_tablero_con_jugador(tablero, pos_jugador)
    mostrar_tablero()
    seguir = desea_seguir_jugando()
guardar_datos(nombre, pos_jugador)
print("Chau!")