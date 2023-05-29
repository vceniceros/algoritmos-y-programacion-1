import doctest
def posibles_amistades(personas, intereses, MINIMO_INTERESES = 2):
    """
    Escribir en Python una función posibles_amistades que recibe dos listas: una de Personas y 
    otra de intereses afines. La lista de Personas intercala nombres con listas de intereses, 
    es decir, en la primera posición tiene un nombre y en la segunda, una lista de intereses, etc.
    La función debe devolver una lista solo con los nombres de las personas que tengan dos o más 
    intereses en común.

    Ejemplos

    >>> Personas = ["Camila", ["natación", "gimnasio", "vol", "futbol"], "Mario", ["natación", "basquet", "gimnasio", "cine"], "Rosa", ["cine", "teatro", "natación" ]] 
    >>> intereses_afines = ["natación", "teatro", "cine", "tenis"]
    >>> intereses_afines2 = ["cine", "tenis", "ajedrez"]
    >>> posibles_amistades(Personas, intereses_afines) 
    ["Mario", "Rosa"]
    >>> posibles_amistades (Personas, intereses_afines2)
    []
    """
    potenciales_amistades = []
    for interes_index in range(1,len(personas),2):
        persona = personas[interes_index-1]
        intereses_comun = 0
        for interes in personas[interes_index]:
            i = 0
            while intereses_comun <= MINIMO_INTERESES and i <= len(personas[interes_index]):
                if interes in intereses:
                    intereses_comun +=1
                    if intereses_comun >= MINIMO_INTERESES:
                        potenciales_amistades.append(persona)
                i += 1
    return potenciales_amistades
doctest.testmod()
