import doctest
def es_binario(entrada):
    """
    >>> es_binario("0A101010111111111011111011111110")
    False
    >>> es_binario("011101")
    True
    >>> es_binario("-1")
    False
    >>> es_binario("@")
    False
    >>> es_binario("1-0")
    False
    >>> es_binario("-011021212")
    False
    >>> es_binario("-0")
    False
    >>> es_binario("1")
    True
    >>> es_binario("0")
    True
    >>> es_binario("0 1")
    False
    """
     #Es verdadero hasta que demuestres lo contrario
    esBinario = True
    i = 0
    if entrada =='':
        esBinario = False
    else:
        while i < len(entrada) and esBinario == True:
            if not (entrada[i] == "1" or entrada[i] == "0"):
                esBinario=False
            i += 1
    return esBinario
print (doctest.testmod())
