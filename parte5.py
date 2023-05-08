

def Puntaje(resultado):
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
def Bucle():
    """
    en esta funcion se establece un bucle donde el usuario indica si quiere seguir jugando
    si aprieta s se sigue sino se corta
    """
    puntos = 0
    decision = 's'
    try:
         while decision != 'n':
        
          decision = input("¿desea seguir jugando?(s para si, n para no): ")
          prueba_res = input("t o f: ")
          if prueba_res == 't':
              prueba_res = True
          else:
              prueba_res = False
          puntos += Puntaje(prueba_res)
    except TypeError:
             print("error de tipado, por favor ingrese s para si o n para no")
             decision = input("¿desea seguir jugando?(s para si, n para no): ")
    return print(puntos)

Bucle()


