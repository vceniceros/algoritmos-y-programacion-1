import doctest
def numeros_al_cuadrado(numero):
    """
    >>> numeros_al_cuadrado(4) 
    {1: 1, 2: 4, 3: 9, 4: 16}
    """
    nc = {}
    for i in range(1,numero+1):
        nc[i]= i*i
    return nc
def mezclar_diccionarios(dicc_uno, dicc_dos):
    """
    >>> dicc_1 = {'clave1': 1, 'clave3': 3}
    >>> dicc_2 = {'clave2': 2, 'clave4': 4}
    >>> mezclar_diccionarios(dicc_1, dicc_2)
    {'clave1': 1, 'clave3': 3, 'clave2': 2, 'clave4': 4}
    """
    dicc = dicc_uno
    dicc.update(dicc_dos)
    return dicc
def filtrar_por_sumar_diez(diccionario):
    """ 
    >>> filtrar_por_sumar_diez({8: 11, 3: 6, 9: 2, 1: 4}) 
    {8: 11, 9: 2}
    """
    dicc = diccionario
    fpsd = {}
    for n in dicc:
        if n.keys()*n.values() > 10:
            fpsd.update(n)
    return fpsd

 
def ordenar_valores_por_longitud(diccionario):
    pass
doctest.testmod()