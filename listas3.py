import doctest
def ordenar_lista_menor_a_mayor(lista):
    """
    >>> ordenar_lista_menor_a_mayor([5,2,6,23,4])
    [2, 4, 5, 6, 23]
    """
    lista.sort()
    return lista

def ordenar_lista_mayor_a_menor(lista):
    """
    >>> ordenar_lista_mayor_a_menor([5,2,6,23,4])
    [23, 6, 5, 4, 2]
    """
    lista.sort()
    lista.reverse()
    return lista

def ordenar_lista_alfabeticamente(lista):
    """
    >>> ordenar_lista_alfabeticamente(["hola", "estas", "como", "si"]) 
    ['como', 'estas', 'hola', 'si']
    """
    lista.sort()
    return lista

def ordenar_palabras_por_longitud(lista):
    """
    >>> ordenar_palabras_por_longitud(["a", "hola", "si", "string largo", "string"]) 
    ['string largo', 'string', 'hola', 'si', 'a']
    """
    lista.sort(key=len)
    lista.reverse()
    return lista
    
def ordenar_lista_por_tupla(lista):
    """
    >>> ordenar_lista_por_tupla([(1,2), (2,3), (6,7), (5,4), (7,1)]) 
    [(6, 7), (5, 4), (2, 3), (1, 2), (7, 1)]
    """
    return sorted(lista, key= lambda lista: lista[1], reverse=True)

def ordenar_lista_por_suma_tupla(lista):
    """
    >>> ordenar_lista_por_suma_tupla([(1, 5), (7, 3), (5, 4), (4, 3)]) 
    [(7, 3), (5, 4), (4, 3), (1, 5)] 
    """
    return sorted(lista, key= lambda lista: lista[0]+lista[1], reverse=True)
doctest.testmod()