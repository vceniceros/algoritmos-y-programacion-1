import doctest
def posibles_amistades(personas, intereses, COINCIDENCIAS_MINIMAS = 2):
    """
    Escribir en Python una función posibles_amistades que recibe dos listas: 
    una de Personas y otra de intereses afines. La lista de Personas intercala nombres
    con listas de intereses, es decir, 
    en la primera posición tiene un nombre y en la segunda, una lista de intereses, etc. 
    La función debe devolver una lista solo con los nombres de las
    personas que tengan dos o más intereses en común.

    Ejemplos:
    >>> Personas = ["Camila", ["natación", "gimnasio", "vol", "futbol"], "Mario", ["natación", "basquet", "gimnasio", "cine"], "Rosa", ["cine", "teatro", "natación" ]] 
    >>> intereses_afines = ["natación", "teatro", "cine", "tenis"]
    >>> intereses_afines2 = ["cine", "tenis", "ajedrez"]
    >>> posibles_amistades (Personas, intereses_afines)
    ['Mario', 'Rosa']
    >>> posibles_amistades (Personas, intereses_afines2)
    []
    """
    posibles_amistades = []
    coincidencia = 0
    for interes in range(1,len(personas),2):
        persona = personas[interes-1]
        for interes_individual in personas[interes]:
            if interes_individual in intereses:
                coincidencia +=1
        if coincidencia >= COINCIDENCIAS_MINIMAS:
            posibles_amistades.append(persona)
    return posibles_amistades

Personas = ["Camila", ["natación", "gimnasio", "vol", "futbol"], "Mario", ["natación", "basquet", "gimnasio", "cine"], "Rosa", ["cine", "teatro", "natación" ]] 
intereses_afines = ["natación", "teatro", "cine", "tenis"]
intereses_afines2 = ["cine", "tenis", "ajedrez"]
print(posibles_amistades(Personas, intereses_afines))
print(posibles_amistades(Personas, intereses_afines2))
doctest.testmod()