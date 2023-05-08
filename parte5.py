
def acumulate_points(results,SUCCESS_POINTS = 10, FAIL_POINTS = -3):
    """
    recibe una tupla con aciertos y errores y devuelve el puntaje total del juego como entero
    """
    SUCCESS_INDEX = 0
    FAIL_INDEX = 1
    success_point = results[SUCCESS_INDEX]*SUCCESS_POINTS
    fail_point = results[FAIL_INDEX]*FAIL_POINTS
    return success_point+fail_point

def play_match():
    """
    le pregunta al jugador si desea seguir jugando y devuelve el puntaje final
    """
    points = 0
    decision = True 
    while decision:
        #TODO: result = aca va la funcion de lucas
        points += acumulate_points(results)
        print(f"Puntaje Final: {points}")
        play_again = str(input("si desea seguir jugando, escriba ok: "))
        if play_again != 'ok':
            decision = False
            
def main():
    """ 
    ejecuta el juego
    """
    play_match()
main()