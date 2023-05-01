import doctest
def numero_complejo(tupla):
    """
    Escribir una función que reciba un número complejo
    representado como una tupla de la forma (parte_real, parte_imaginaria) 
    y devuelva su representación binómica en una cadena. Ejemplo:
    >>> primer_numero = (1,3)
    >>> segundo_numero = (0,3)
    >>> tercero_numero = (1,-3)
    >>> cuarto_numero = (-1,3)
    >>> quinto_numero = (1,0)
    >>> numero_complejo(primer_numero)
    '1+3i'
    >>> numero_complejo(segundo_numero)
    '3i'
    >>> numero_complejo(tercero_numero)
    '1-3i'
    >>> numero_complejo(cuarto_numero)
    '-1+3i'
    >>> numero_complejo(quinto_numero)
    '1'
    """
    REAL = 0
    IMAGINARIO = 1
    complejo = ''
    if tupla[REAL] > 0 and tupla[IMAGINARIO] > 0 or tupla[REAL] < 0 and tupla[IMAGINARIO] > 0:
         complejo = str(tupla[REAL])+'+'+str(tupla[IMAGINARIO])+'i' 
    
    elif  tupla[REAL] > 0 and tupla[IMAGINARIO] < 0:
         complejo = str(tupla[REAL])+str(tupla[IMAGINARIO])+'i' 
    
    elif  tupla[REAL] == 0 :
         complejo = str(tupla[IMAGINARIO])+'i' 
    
    elif  tupla[IMAGINARIO] == 0 :
         complejo = str(tupla[REAL])     
    
    return complejo


def numeros_negativos(lista):
     """
     Escribir una función que reciba una 
     lista de números enteros y devuelva la cantidad de números negativos pares en ella.

     >>> lista_1 = [1, -2, 4, -3, -4, -6, 10, 21, 22]
     >>> lista_2 = [-2, -4, 2, 6, 3, 5, 7, 21, -9, -7]
     >>> numeros_negativos(lista_1)
     [-2, -4, -6]
     >>> numeros_negativos(lista_2)
     [-2, -4]
     """
     pares = [x for x in lista if x < 0 and x%2==0]
     return pares
def rotaciones(palabra):
     """
     >>> pala = 'rotar'
     >>> rotaciones(pala)
     ['rotar', 'otarr', 'tarro', 'arrot', 'rrota']
     """
     lista = []
     for i in range(len(palabra)):
          lista.append(palabra[i:]+palabra[:i])
     return lista
def frecuencia(texto):
     """
     Escribir una función que dado un texto, 
     devuelva un diccionario con la frecuencia de cada palabra del texto.

     >>> palabra = 'se viene boca se viene boca esto es boca aguante boca'
     >>> frecuencia(palabra)
     {'se': 2, 'viene': 2, 'boca': 4, 'esto': 1, 'es': 2, 'aguante': 1}
     """
     dicc = {}
     palabras = texto.split()
     for palabra in palabras:
            dicc.update({palabra: texto.count(palabra)})
     return dicc
def lista_max_frecuencia(texto):
     """
     b. Escribir una función que reciba un diccionario como el generado por la función del ítem a
       y devuelva una lista con la/s palabras que tienen la máxima frecuencia.
    >>> palabra = 'se viene boca se viene boca esto es boca aguante boca'
    >>> lista_max_frecuencia(palabra)
    ['boca']
     """
     dicc = frecuencia(texto)
     mayor = []
     lista = dicc.items()
     for palabra in lista:
          max_count = 0
          palabra_mas_contada = ''
          if palabra[1] > max_count:
               palabra_mas_contada = palabra[0]
     mayor.append(palabra_mas_contada)
     return mayor
doctest.testmod()