from library import *

def desea_seguir_jugando():
    respuesta = input("desea seguir jugando? (s/n)\n- - ->: ").lower()
    while respuesta != "s" and respuesta != "n" and respuesta != "si" and respuesta != "no" and respuesta != "sí":
        print("respuesta invalida, ingrese s/n")
        respuesta = input("desea seguir jugando? (s/n)\n- - ->: ").lower()
    
    resultado = "s" if respuesta == "s" or respuesta == "si" or respuesta == "sí" else "n"
    return resultado

def nombre_usuario():
    nombre = input("cual es su nombre?\n- - ->: ")
    while nombre == "":
        print("el nombre no puede estar vacio, intente nuevamente")
        nombre = input("cual es su nombre?\n- - ->: ")
    return nombre


def respuesta_valida_opcion(texto):
    respuesta = input(texto).upper()
    while respuesta != "A" and respuesta != "B" and respuesta != "C":
        print("respuesta invalida, ingrese A, B o C.")
        respuesta = input(texto).upper()
    return respuesta

def verificar_estado_juego(posicion:int, nombre:str, tablero:list):
    estado = "continua"

    if posicion == len(tablero)-1:
        print(f"felicidades {nombre}, llegaste al final y ganaste el juego")
        estado = "gano"
    elif posicion == 0:
        print(f"lo siento {nombre}, perdiste el juego")
        estado = "perdio"

    return estado
