import doctest
def ultimos_tres_elementos(lista):
    """
    >>> ultimos_tres_elementos([5,3,6,2,5,32,6,4,7]) 
    [6, 4, 7]
    """
    return lista[-3:]

def ultimos_tres_elementos_concatenados(lista):
    """
    >>> ultimos_tres_elementos_concatenados([[1,2,3,4], [5,6,7,8], [9,10,11,12]]) 
    [2, 3, 4, 6, 7, 8, 10, 11, 12]
    """
    
    return lista[-3:] 

def indices_pares(lista):
    pass
    
def indices_impares(lista):
    pass

def invertir(lista):
    pass
doctest.testmod()