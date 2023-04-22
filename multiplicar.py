def multiplicar (a, b):
    """multiplica
    >>>multiplicar(2,2)
    4
    >>> multiplicar(3,-2)
    -6
    >>> multiplicar(-3,-2)
    6
    >>>multiplicar(-3,2)
    -6
"""

    respuesta = 0
    for i in range(1, b+1):
        respuesta = respuesta+a
    return respuesta



import doctest
print(doctest.testmod())
