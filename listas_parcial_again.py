import doctest
def posibles_amistades(persona,intereses, MIN_INTERES = 3):
    """
    >>> Personas = ["Camila", ["natación", "gimnasio", "vol", "futbol"], "Mario", ["natación", "basquet", "gimnasio", "cine"], "Rosa", ["cine", "teatro", "natación" ]] 
    >>> intereses_afines = ["natación", "teatro", "cine", "tenis"]
    >>> intereses_afines2 = ["cine", "tenis", "ajedrez"]
    >>> posibles_amistades (Personas, intereses_afines)
    ['Mario', 'Rosa']
    >>> posibles_amistades (Personas, intereses_afines2)
    []
    """
    posible_amistad = []
    coincidencia = 0
    for interes_index in range(1,len(persona),2):
        nombre = persona[interes_index-1]
        for interes in persona[interes_index]:
            if interes in intereses:
                coincidencia += 1
        if coincidencia >= MIN_INTERES:
            posible_amistad.append(nombre)
    return posible_amistad
doctest.testmod()