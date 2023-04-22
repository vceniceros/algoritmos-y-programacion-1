#crear diccionario con ciudades como clave y poblacion y parametro como vzlores, ordenarlos de mayor a menor votantes
import doctest
def contar_votantes(votantes):
    """
    >>> votantes={"cordoba":[3000000,400000],"buenos aires":[14000000,120000],"la matanza":[20000000,30000]}
    >>> contar_votantes(votantes)
    [('cordoba', [3000000, 400000]), ('buenos aires', [14000000, 120000]), ('la matanza', [20000000, 30000])]
    """
    lista = votantes.items()
    lista_ordenada = sorted(lista,key= lambda x: x[1][1] ,reverse=True)
    return lista_ordenada
doctest.testmod()