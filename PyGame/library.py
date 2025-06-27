from preguntas import preguntas
import random
from validaciones import respuesta_valida_opcion
pos_jugador = 15
tablero = [0,1,0,0,0,3,0,0,0,0,0,1,0,0,2,1,1,0,0,0,1,0,0,2,0,0,0,1,0,0,0]
preguntas_hechas = []

def hacer_preguntas(nombre:str):
    """
    Funcion que se encarga realizar preguntas randoms
    """
    pregunta = random.choice(preguntas)
    while pregunta in preguntas_hechas:
        pregunta = random.choice(preguntas)

    preguntas_hechas.append(pregunta)

    print(f"""
        {pregunta["pregunta"]}
        A) {pregunta["respuesta_a"]} 
        B) {pregunta["respuesta_b"]}
        C) {pregunta["respuesta_c"]}
            """)
    respuesta = respuesta_valida_opcion(f"cual es tu respuesta {nombre}? (A, B o C)\n- - ->: ")
    return respuesta.upper() == pregunta["respuesta_correcta"].upper()


def mostrar_tablero():
    """
    funcion encargada de mostrar el tablero
    """
    for i in range(len(tablero)):
        print(tablero[i], end=" ")
    print()

# def movimiento(posicion, resultado):
#     """
#     funcion que realiza el movimiento dependiendo si el usuario acierta o no la respuesta
#     """
#     if resultado:
#         posicion += 1
#         print("Correcto, avanzas")

#         if posicion >= len(tablero):
#             posicion = len(tablero) - 1

#         casillero_actual = tablero[posicion]
#         while casillero_actual != 0:
#             if casillero_actual >= 0:
#                 posicion += casillero_actual
#                 print(f"Avanzas {casillero_actual} casilleros extras")
#             else:
#                 print(f"Retrocedes {abs(casillero_actual)} casilleros")
#                 posicion -= casillero_actual

#             if posicion < 0:
#                 posicion = 0
#                 break
#             if posicion >= len(tablero):
#                 posicion = len(tablero) - 1
#                 break

#             casillero_actual = tablero[posicion]

#     else:
#         posicion -= 1
#         print("Incorrecto, retrocedes")
#         if posicion < 0:
#             posicion = 0

#     return posicion

def movimiento(posicion, resultado):
    if resultado:
        posicion += 1
        print("Respuesta correcta, avanzas")
        casillero_actual = tablero[posicion]
        while casillero_actual != 0:
            print(f"Correcto! avanzas {casillero_actual} casilleros extras")
            posicion += casillero_actual
            casillero_actual = tablero[posicion]
    else:
        posicion -= 1
        print("Respuesta incorrecta, retrocedes")
        casillero_actual = tablero[posicion]
        while casillero_actual != 0:
            print(f"Incorrecto! retrocedes {casillero_actual} casilleros extras")
            posicion -= casillero_actual
            casillero_actual = tablero[posicion]
    return posicion

def mostrar_tablero_con_jugador(tablero:list, pos_jugador:int):
    """
    funcion que se encarga de mostrar donde esta situado el jugador en el tablero
    """
    for i in range(len(tablero)):
        if i == pos_jugador:
            print(f"P", end=" ")
        else:
            print("_", end=" ")
    print()