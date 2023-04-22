"""
https://www.myrpl.ar/courses/34/activities/5062

Completar el cuerpo de la función. La misma recibe como parámetro dos números que serán tomados como límite inferior y límite superior del cálculo que debemos realizar.
La función debe retornar la mayor distancia entre dos números primos existentes entre dichos límites, incluyéndolos.
Recordar que el 1 no es primo y el 2 sí lo es. Se puede asumir que los parámetros de entrada han sido validados previamente.
Si en el rango existiera un solo número primo hay que devolver 0.
Si en el rango no hay ningún número primo hay que devolver -1.

Ejemplos:

mayor_distancia_entre_primos(1, 3) => 1 (distancia entre 2 y 3)
mayor_distancia_entre_primos(1, 5) => 2 (distancia entre 3 y 5)
mayor_distancia_entre_primos(1, 15) => 4 (distancia entre 7 y 11)
mayor_distancia_entre_primos(14, 18) => 0 (hay un solo número primo)
mayor_distancia_entre_primos(14, 16) => -1 (no hay números primos)

Ayuda: Pueden utilizar la función es_primo(numero) definida en actividades anteriores de la categoría, logrando un mayor grado de modularización.
"""


def es_primo(numero):
    es_primo = True
    if numero <= 1:
        es_primo = False
    for i in range(2, numero):
        if numero % i == 0:
            es_primo = False
    return es_primo


def mayor_distancia_entre_primos(inferior, superior):
    distancia = -1
    primo_mas_reciente = None
    for i in range(inferior, superior + 1):
        # print("i:", i, "primo_mas_reciente:", primo_mas_reciente, "distancia:", distancia, "primo:", es_primo(i))
        if es_primo(i):
            if primo_mas_reciente is None:
                # si hay al menos un primo la distancia no va a ser -1
                distancia = 0
            else:
                nueva_distancia = i - primo_mas_reciente
                if nueva_distancia > distancia:
                    distancia = nueva_distancia
            primo_mas_reciente = i
    return distancia
