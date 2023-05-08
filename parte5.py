def puntaje(resultado):
    """
    esta funcion recibira un booleano dependiendo del acierto o desacierto del jugador,
    si acierta sera verdadero y si le erra sera falso, de esto dependera la suma o el resto de puntajes
    """
    suma_punto = 0
    if resultado:
        suma_punto += 10
    else:
        suma_punto-=3
    return suma_punto
