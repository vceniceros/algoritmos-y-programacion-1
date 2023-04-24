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
doctest.testmod()