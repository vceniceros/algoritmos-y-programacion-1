import doctest
from string import ascii_lowercase
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
    [('boca', 4)]
     """
     dicc = frecuencia(texto)
     mayor = []
     CONTEO = 1
     PALABRA = 0
     palabra_mas_contada = ''
     max_count = 0
     for palabra in dicc.items():
          if palabra[CONTEO] > max_count:
               max_count = palabra[CONTEO]
     mayor = [x for x in dicc.items() if x[CONTEO] == max_count]
     return mayor
def palindromo(texto):
     """
     >>> frase = 'con mis amigos nos fuimos de viaje a neuquen'
     >>> palindromo(frase)
     ['neuquen']
     """
     lista = []
     ULTIMA_LETRA = -1
     palabras = texto.split()
     for palabra in palabras:
          if palabra==palabra[::ULTIMA_LETRA] and len(palabra) > 1:
               lista.append(palabra)
     return lista
def pangrama(texto):
     """
     >>> texto_1 = 'sabrina te amo'
     >>> texto_2 = 'the quick brown fox jumps over the lazy dog'
     >>> pangrama(texto_1)
     False
     >>> pangrama(texto_2)
     True
     """
     resutado = False
     letras = []
     for i in range(len(texto)):
          if texto[i] not in letras and texto[i] != ' ':
               letras.append(texto[i])
     if len(letras) == len(ascii_lowercase):
          resutado = True
     return resutado
def dias_de_juntada(diccionario):
     """
     >>> dias = { 'Juan': ['MIE', 'VIE', 'SAB'], 'Jose': ['VIE', 'SAB', 'DOM'], 'Jorge': ['JUE', 'VIE', 'SAB'] }
     >>> dias_de_juntada(dias)
     ['VIE', 'SAB']
     """
     dias_disponibles = []
     dias_juntada = []

     for dias in diccionario.values():
          if dias not in dias_disponibles:
               dias_disponibles+=dias
     for dias in dias_disponibles:
          if dias not in dias_juntada and dias_disponibles.count(dias) == len(diccionario):
               dias_juntada.append(dias)
     return dias_juntada
def es_un_pelotudo(cosas_que_hace,cosas_de_pelotudo):
     """
     >>> cosas_hechas = {'que no se disculpe': 2, 'ser peronista': 3, 'ser infiel': 0, 'que digas que star wars es ciencia ficcion': 1, 'recicla': 3, 'trata bien a su novia': 10}
     >>> cosas_pelotudas = ['que no se disculpe', 'ser peronista', 'ser infiel', 'que digas que star wars es ciencia ficcion']
     >>> es_un_pelotudo(cosas_hechas,cosas_pelotudas)
     True
     >>> cosas_pelotudas_sabri = ['no entender indirectas', 'cortar conversaciones', 'ignorarme']
     >>> cosas_que_hago = {'no entender indirectas': 5, 'cortar conversaciones': 3, 'ignorarme': 3, 'darme amor': 4}
     >>> es_un_pelotudo(cosas_que_hago, cosas_pelotudas_sabri)
     True
     """
     acumulacion_de_pelotudeces = 0
     cantidad_de_pelotudeces_por_dia = 0
     CONSTANTE_PELOTUDA = 3
     resultado = False
     for pelotudes in cosas_que_hace.keys():
          if pelotudes in cosas_de_pelotudo:
               acumulacion_de_pelotudeces+=1
     for cantidad in cosas_que_hace.values():
          if cantidad >= CONSTANTE_PELOTUDA:
               cantidad_de_pelotudeces_por_dia+=1
     if cantidad_de_pelotudeces_por_dia*acumulacion_de_pelotudeces > len(cosas_que_hace):
          resultado = True
     return resultado
doctest.testmod() 