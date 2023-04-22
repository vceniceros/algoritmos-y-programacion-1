import doctest
def palabra_mas_larga(texto):
    """
    >>> palabra_mas_larga("Hola como estas este es un texto de prueba")
    prueba
    """
    la_mas_larga = ""
    palabra = texto.split()
    print(palabra)
    return la_mas_larga
doctest.testmod()