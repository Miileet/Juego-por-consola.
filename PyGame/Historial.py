def guardar_datos(nombre:str, puntos:int):
    with open("Score.csv", "a") as puntajes:
        puntajes.write(f"{nombre},{puntos}\n")