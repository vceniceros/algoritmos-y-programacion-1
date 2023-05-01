import doctest
def ordenar_usuarios(lista):
    """
    >>> lista_1 = ["manu", "diego", "fede", "agus", "charly"]
    >>> ordenar_usuarios(lista_1)
    ['Agus', 'Charly', 'Diego', 'Fede', 'Manu']
    """
    PRIMERA_LETRA = 0
    nueva_lista = []
    for palabra in lista:
        palabra = palabra[PRIMERA_LETRA].upper()+palabra[1:]
        nueva_lista.append(palabra)
    nueva_lista.sort()
    return nueva_lista
def reordenar_pares(lista):
    """
    >>> reordenar_pares([3,5,2,6,18,7,40,11])
    [2, 6, 18, 40, 3, 5, 7, 11]
    """
    lista_pares = [x for x in lista if x%2 ==0]
    lista_impares = [x for x in lista if x not in lista_pares]
    lista_mezcla = lista_pares+lista_impares
    return lista_mezcla
def calificando_restaurantes(diccionario):
    """
    >>> dicc = {'La Mazorca': 1, 'Lemonmay': 4, 'Las Cumbres': 4}
    >>> calificando_restaurantes(dicc)
    {1: ['La Mazorca'], 4: ['Lemonmay', 'Las Cumbres']}
    """
    restaurantes = diccionario.items()
    dicc = {}
    NOTA = 1
    RESTAURANTE = 0
    for restaurante in restaurantes:
       if restaurante[NOTA] not in dicc:
           restaurantes_por_punto = []
           dicc.update({restaurante[NOTA]: [restaurante[RESTAURANTE]]})
       else:
           dicc[restaurante[NOTA]]+=[restaurante[RESTAURANTE]]
    return dicc
doctest.testmod()