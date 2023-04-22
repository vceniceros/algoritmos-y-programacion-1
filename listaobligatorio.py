import doctest
def es_primo(numero):
    #tu codigo
     """valora si es primo"""
     es_primo = True 
     if numero <= 1:
         es_primo = False
     for i in range(2,numero): 
         if numero % i==0:
            es_primo= False
     return es_primo
   
def filtrar_primos(numeros, menor_numero):
    """
    >>> filtrar_primos([3, 7, 11, 13], 8) 
    [11, 13]
    >>> filtrar_primos([11, 7, 3, 19], 15) 
    [19]
   """
    primos = [x for x in numeros if es_primo(x)==True and x > menor_numero]
    return primos
def ordenar_por_longitud_de_tuplas(tuplas):
    """
    >>> lista_tuplas = [(1,5,6), (1,2), (1,), (6,4,5,6), ("asd", 9, 5.6, "l", "s")]
    >>> ordenar_por_longitud_de_tuplas(lista_tuplas) 
    [('asd', 9, 5.6, 'l', 's'), (6, 4, 5, 6), (1, 5, 6), (1, 2), (1,)]
    """
    return sorted(tuplas, key= len,reverse=True)
def concatenar_primeros_elementos(lista):
    """
    >>> lista = [[1,4,5,6], [2,3,4,5], [6,4,4,6,7,8], [5,6,7,3,5,6,4]]
    >>> concatenar_primeros_elementos(lista) 
    [1, 4, 5, 2, 3, 4, 6, 4, 4, 5, 6, 7]
    """
    listota = []
    for listita in lista:
        listota += listita[0:3]
    return listota
doctest.testmod()