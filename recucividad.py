import doctest
def sumar(lista, n):
    """
En este ejercicio la función debe devolver la suma de los n
primeros elementos de una lista de enteros de manera recursiva.
La función recibe una lista de enteros y una cantidad n, 
la función debe devolver la suma de los n primeros elementos de la lista.
Ejemplos

Nota: no solo tiene que pasar las pruebas, sino que hay que resolverlo recursivamente.
    >>> sumar([5,2,6,23,4], 3)
    13
    >>> sumar([5,2,6,23,4], 1) 
    5
    >>> sumar([5,2,6,23,4], 0)
    0
    >>> sumar([5,2,6,23,4], 5)
    40
"""
    if n == 0:
        return 0
    else: 
        return lista[n-1] + sumar(lista,n-1)
doctest.testmod()