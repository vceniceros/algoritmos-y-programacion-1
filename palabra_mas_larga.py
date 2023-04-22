import doctest
def palabra_mas_larga(texto):
    """
    >>> palabra_mas_larga("Hola como estas este es un texto de prueba")
    prueba
    """
    palabra = texto.split()  
    mayor = ""
    for i in palabra:
        if len(i) > len(mayor):
            mayor = i
    return mayor
doctest.testmod()