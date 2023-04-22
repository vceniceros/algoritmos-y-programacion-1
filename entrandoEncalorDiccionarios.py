import doctest
def numeros_al_cuadrado(numero):
    """ 
    >>> numeros_al_cuadrado(4) 
    {1: 1, 2: 4, 3: 9, 4: 16}
    """
    cuadrado = {}
    for i in range(1,numero+1):
        cuadrado[i]=i*i
    return cuadrado

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
    dicc = {}
    lista = diccionario.items()
    suma_diez = [x for x in lista if x[0]+x[1] >=10]
    dicc.update(suma_diez)
    return dicc 
def ordenar_valores_por_longitud(diccionario):
    """
    >>> dicc = {'boca':'river', 'pablo':'guarna', 'hola':'algoritmos'}
    >>> dicc2 = {'1':'k', '2':'kkk', '3':'kk', '4': 'kkkk'}
    >>> ordenar_valores_por_longitud(dicc) 
    ['algoritmos', 'guarna', 'river']
    >>> ordenar_valores_por_longitud(dicc2) 
    ['kkkk', 'kkk', 'kk', 'k']
    """
    diccvalues = diccionario.values()
    lista = [x for x in diccvalues]
    lista.sort(key=len,reverse=True)
    return lista
    
doctest.testmod()