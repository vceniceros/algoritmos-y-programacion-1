import doctest
def filtrar_pares(lista):
    """
    >>> filtrar_pares([5,6,13,7,11,9,10,11])
    [6, 10]
    """
    lista_pares = []
    for elemento in lista:
        if elemento%2==0:
            lista_pares.append(elemento)
    return lista_pares

def es_primo(numero):
        es_primo = True 
        if numero <= 1:
         es_primo = False
        for i in range(2,numero): 
          if numero % i==0:
            es_primo= False
        return es_primo


def filtrar_primos(lista):
    """
    >>> filtrar_primos([5,6,13,7,11,9,10,11])
    [5, 13, 7, 11, 11]
    """
    lista_primos = []
    for elemento in lista:
        if es_primo(elemento) == True:
            lista_primos.append(elemento)
    return lista_primos

def sumar_elementos(lista):
    """
    >>> sumar_elementos([5,6,13,7,11,9,10,11]) 
    72
    """
    suma_elementos = 0
    for elemento in lista:
        suma_elementos += elemento
    return suma_elementos
def esta_ordenada(lista):
     """
     >>> esta_ordenada([5,6,13,7,11,9,10,11]) 
     False
     >>> esta_ordenada([5,6,7,11])
     True
     """
     lista_ordenada = True
     i = 0
     while i < len(lista)-1 and lista_ordenada == True:
         if lista[i] > lista[i+1]:
             lista_ordenada = False
         i+=1
     return lista_ordenada
def producto_escalar(vector_1, vector_2):
    """
    >>> producto_escalar([2,5,3], [4,6,7]) 
    59
    """
    producto = 0
    for i in range(len(vector_1)):
        producto += vector_1[i]*vector_2[i]
    return producto
def letras_en_palabra(letras, frase):
    #si la letra esta en frase, se coloca en el comprobante. se compara el comprobante y letras al final.
    lista_comprobante=[]
    for i in letras:
        if i in frase:
            lista_comprobante.append(i)
    return letras==lista_comprobante
doctest.testmod()

