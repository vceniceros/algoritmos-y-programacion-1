import doctest
def validar_clave(clave):
    """
    8a 12 long
    una may
    un min
    un numero
    simbololos = ['*','-','$','@']
    no tildes
    no espacios
    >>> clave1 = 'Algoritmo$1'
    >>> clave2 = 'Aprobe-con-7'
    >>> clave3 = 'Aprobé-con-7'
    >>> clave4 = 'Algoritmo $1'
    >>> validar_clave(clave1)
    True
    >>> validar_clave(clave2)
    True
    >>> validar_clave(clave3)
    False
    >>> validar_clave(clave4)
    False
    """
    MAX_LONG = 12
    MIN_LONG = 8
    SIMBOLOS = ['*','-','$','@']
    TILDES = ['á','é','í','ó','ú','Á','É','Í','Ó','Ú']
    cont_min = cont_may = cont_num = cont_car = cont_tildes = cont_espacios = i = 0
    resultado = False
    long_clave = len(clave)
    while long_clave >= MIN_LONG and long_clave <= MAX_LONG and i < long_clave:
        if clave[i] == ' ':
            cont_espacios +=1
        elif clave[i] in TILDES:
            cont_tildes +=1
        elif clave[i].isupper():
            cont_may +=1
        elif clave[i].islower():
            cont_min +=1
        elif clave[i].isnumeric():
            cont_num +=1
        elif clave[i] in SIMBOLOS:
            cont_car +=1
        i+=1
    if cont_may >=1 and cont_min >=1 and cont_num >=1 and cont_car >= 1 and cont_espacios == cont_tildes == 0:
        resultado = True
    return resultado
def elegir(lista_1,lista_2,cuota):
    """
    >>> lista_1 = ["natación", "gimnasio", "voley", "futbol"]
    >>> lista_2  = ["natación", "voley", "gimnasio"] 
    >>> lista_3 = ["natación", "futbol", "karate"]
    >>> elegir(lista_1, lista_2, 5000) 
    True
    >>> elegir(lista_2, lista_3,100)
    False
    """
    MAX_CUOTA = 5500
    resultado = False
    actividades_deseadas = len(lista_2)
    contador = 0
    for actividad in lista_1:
        if actividad in lista_2:
            contador += 1
    if contador >= actividades_deseadas and cuota <= MAX_CUOTA:
        resultado = True
    return resultado
def procesar_partidos(lista):
    """
    >>> lista_1 = [["PP", 19, 35], ["PSOE", 20, 30], ["VOX", 15, 15], ["PP", 0, 151],["PSOE", 20, 0],["VOX", 0, 11]]
    >>> procesar_partidos(lista_1)
    {'PP': 205, 'PSOE': 70, 'VOX': 41}
     """
    dicc = {}
    PARTIDO = 0
    DIPUTADOS = 1
    SENADORES = 2
    SUMA=1
    for mesa in lista:
        if mesa[PARTIDO] not in dicc:
            dicc[mesa[PARTIDO]]=mesa[DIPUTADOS]+mesa[SENADORES]
        else:
            dicc[mesa[PARTIDO]]+=mesa[DIPUTADOS]+mesa[SENADORES]
    return dicc
def ordenar(lista):
    """
    >>> lista_1 = [["PP", 19, 35], ["PSOE", 20, 30], ["VOX", 15, 15], ["PP", 0, 151],["PSOE", 20, 0],["VOX", 0, 11]]
    >>> ordenar(lista_1)
    [('PP', 205), ('PSOE', 70), ('VOX', 41)]
    """
    SUMA_VOTOS = 1
    dicc = procesar_partidos(lista)
    lista_votos = sorted(dicc.items(),key= lambda x: x[SUMA_VOTOS], reverse=True)
    return lista_votos
doctest.testmod()