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
    >>> lista_1 = [["Juan",10],["Mariano",4],["Pepe",7],["Juan",8],["Mariano",7],["Pepe",9],["Juan",9],["Mariano",6],["Pepe",8]]
    >>> diccionario(lista_1) 
    {'Juan': [27, 3, 9], 'Mariano': [17, 3, 5], 'Pepe': [24, 3, 8]}
    """
    PARTICIPANTE = 0
    PUNTO = 1
    PROMEDIO = 2
    dicc = {}
    SUMA_PUNTOS = 0
    CANTIDAD = 1
    for voto in votaciones:
       suma_notas = voto[PUNTO]
       cantidad = 1
       if voto[PARTICIPANTE] not in dicc:
           dicc[voto[PARTICIPANTE]]=[suma_notas,cantidad,suma_notas]
       else:
           dicc[voto[PARTICIPANTE]][SUMA_PUNTOS]+=suma_notas
           dicc[voto[PARTICIPANTE]][CANTIDAD]+=1
           dicc[voto[PARTICIPANTE]][PROMEDIO] = dicc[voto[PARTICIPANTE]][SUMA_PUNTOS]
           dicc[voto[PARTICIPANTE]][PROMEDIO] = dicc[voto[PARTICIPANTE]][PROMEDIO]/dicc[voto[PARTICIPANTE]][CANTIDAD]
           dicc[voto[PARTICIPANTE]][PROMEDIO] = int(dicc[voto[PARTICIPANTE]][PROMEDIO])
    return dicc
def promedio(lista):
    """
    >>> lista_1 = [["Juan",10],["Mariano",4],["Pepe",7],["Juan",8],["Mariano",7],["Pepe",9],["Juan",9],["Mariano",6],["Pepe",8]]
    >>> promedio(lista_1)
    [('Juan', 9), ('Pepe', 8), ('Mariano', 5)]
    """
    PUNTOS = 1
    PROMEDIO = 2 
    dicc = diccionario(lista)
    promedios = sorted(dicc.items(),key=lambda x: x[PUNTOS][PROMEDIO],reverse=True)
    resultado = [(nombre, prom[PROMEDIO]) for (nombre,prom) in promedios]
    return resultado
doctest.testmod()