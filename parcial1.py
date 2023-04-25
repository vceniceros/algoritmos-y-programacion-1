import doctest
        
def contar(cadena):
    """
    >>> contar("aaaáb")
    2
    >>> contar("1+#/_")
    0
    >>> contar("algoritmos y programacion 1")
    13
    """
    lista = []
    for letra in cadena:
        if letra not in lista and letra.isalpha() and letra not in ('á','é','í','ó','ú'):
            lista += letra
    return len(lista)
def elegir(actividades_de_ciudad,actividades_deseadas,costo_por_actividad):
    """
    >>> lista_1 = ["museo","senderismo","bares","montañismo"]
    >>> lista_2 = ["bares","senderismo","museo","conciertos"]
    >>> lista_3 = ["museo","conciertos","bares"]
    >>> elegir(lista_1,lista_2, 5000)
    True
    >>> elegir(lista_1,lista_3, 1000)
    False
    >>> elegir(lista_1,lista_2, 10000)
    False
    """
    COSTO_MAX = 20000
    CANTIDAD_MINIMA_ACTIVIDADES = 3
    actividades_en_comun = 0
    for actividad in actividades_de_ciudad:
        if actividad in actividades_deseadas:
            actividades_en_comun +=1
    return actividades_en_comun >= CANTIDAD_MINIMA_ACTIVIDADES and costo_por_actividad*actividades_en_comun <= COSTO_MAX
def diccionario(votaciones):
    """
    >>> lista_1 = [["Juan",10],["Mariano",4],["Pepe",7]]
    >>> lista_2 = [["Juan",8],["Mariano",7],["Pepe",9]]
    >>> lista_3 = [["Juan",9],["Mariano",6],["Pepe",8]]
    >>> lista_4 = [["Juan",7],["Mariano",1],["Pepe",5]]
    >>> lista_5 = [["Juan",10],["Mariano",5],["Pepe",9]]
    >>> diccionario(lista_1)
    {'Juan': 10, 'Mariano': 4, 'Pepe': 7}
    >>> diccionario(lista_3)
    {'Juan': 9, 'Mariano': 6, 'Pepe': 8}
    """
    dicc = {}
    PARTICIPANTE = 0
    PUNTO = 1
    for voto in votaciones:
       if voto[PARTICIPANTE] in dicc:
           dicc[voto[PARTICIPANTE]]+=voto[PUNTO]
       else:
           dicc[voto[PARTICIPANTE]]=voto[PUNTO]
    return dicc
def promedio(puntajes):
    """
    >>> lista_1 = [["Juan",10],["Mariano",4],["Pepe",7]]
    >>> lista_2 = [["Juan",8],["Mariano",7],["Pepe",9]]
    >>> lista_3 = [["Juan",9],["Mariano",6],["Pepe",8]]
    >>> promedio(lista_1)
    []
    """
doctest.testmod()