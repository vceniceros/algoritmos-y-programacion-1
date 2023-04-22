import doctest
def numeros_positivos(numeros):
    """
    >>> numeros_positivos(5) 
    [1, 2, 3, 4, 5]
    """
    positivos= [x for x in range(1,numeros+1)]
    return positivos
def numeros_positivos_pares(numero):
    """
    >>> numeros_positivos_pares(7)
    [2, 4, 6]
    """
    pares = [ x for x in numeros_positivos(numero) if x%2 ==0]
    return pares
def numeros_positivos_pares_cuadrado(numero):
     """
    >>> numeros_positivos_pares_cuadrado(7)
    [4, 16, 36]
    """
     cuadrado = [x*x for x in numeros_positivos_pares(numero)]
     return cuadrado
def impares_al_cuadrado(lista):
     """ 
     >>> impares_al_cuadrado([1,2,3,4,5,6,7]) 
     [1, 2, 9, 4, 25, 6, 49]
     """
     lista = [x*x if x%2 !=0 else x for x in lista ]
     return lista
def filtrar_tuplas_por_suma(lista_de_tuplas):
     """
     >>> filtrar_tuplas_por_suma([(3, -3), (4, -5), (1, 2), (1, -2)]) 
     [(1, 2)]
     """
     lista_de_tuplas = [(x,y) for (x,y) in lista_de_tuplas if x+y >= 0]
     return lista_de_tuplas
def filtrar_tupla_elemento_par(lista_de_tuplas):
    """
    >>> filtrar_tupla_elemento_par([(7, -5), (4, 5), (1, 2), (1, -3), (4, 2)]) 
    [(4, 5), (1, 2), (4, 2)]
    """
    lista_de_tuplas = [(x,y) for (x,y) in lista_de_tuplas if x%2==0 or y%2==0]
    return lista_de_tuplas
doctest.testmod()