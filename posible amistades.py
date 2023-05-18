import doctest
def posibles_amistades(personas, intereses):
    """
    Escribir en Python una función posibles amistades que recibe dos listas: una de Personas y otra
    de intereses afines. La lista de Personas intercala nombres con listas de intereses, es decir, 
    en la primera posición tiene un nombre y en la segunda, una lista de intereses, etc. La función debe
    devolver una lista solo con los nombres de las personas que tengan dos o más intereses en común.
    Ejemplos:
    Personas = 
    ['Camila', ['natación', 'gimnasio', 'voley', 'futbol'], 'Mario', ['natación', 'basquet', 'gimnasio', 'cine'], 'Rosa', ['cine', 'teatro', 'natación' ]]
    intereses_afines = ['natación', 'teatro', 'cine', 'tenis']
    intereses afines2 = ['cine', 'tenis', 'ajedrez']
    posibles_amistades (Personas, intereses_afines) 
    ['Mario', 'Rosa']
    posibles_amistades (Personas, intereses_afines2)
    []
    """
    pass

def personas_diccionario(personas):
    """
 
    """
    dicc = {}
    for persona_interes in range(1,len(personas),2):
        dicc[personas[persona_interes-1]]=personas[persona_interes]
    return dicc
def posibles_amistades(personas, intereses):
    """
    Escribir en Python una función posibles amistades que recibe dos listas: una de Personas y otra
    de intereses afines. La lista de Personas intercala nombres con listas de intereses, es decir, 
    en la primera posición tiene un nombre y en la segunda, una lista de intereses, etc. La función debe
    devolver una lista solo con los nombres de las personas que tengan dos o más intereses en común.
    Ejemplos:
    >>> Personas = ['Camila', ['natación', 'gimnasio', 'voley', 'futbol'], 'Mario', ['natación', 'basquet', 'gimnasio', 'cine'], 'Rosa', ['cine', 'teatro', 'natación' ]]
    >>> intereses_afines = ['natación', 'teatro', 'cine', 'tenis']
    >>> intereses_afines2 = ['cine', 'tenis', 'ajedrez']
    >>> posibles_amistades (Personas, intereses_afines) 
    ['Mario', 'Rosa']
    >>> posibles_amistades (Personas, intereses_afines2)
    []
    """
    dicc = personas_diccionario(personas)
    potenciales_amigos = []
    PERSONA = 0
    MIN_COINCIDENCIA = 2
    i = 0
    while i <= len(dicc.values()) and coincidencia < 2:
       for persona_interes in dicc: 
        for intereses in dicc.values():
            for interes in range(0,len(intereses)):
                coincidencia = 0
                if intereses[interes] in intereses:
                    coincidencia+=1
                if coincidencia == MIN_COINCIDENCIA:
                    potenciales_amigos.append(persona_interes[PERSONA])
        i+=1
    return potenciales_amigos


doctest.testmod()