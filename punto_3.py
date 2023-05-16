import random
import string

def ObtenerLetras(letras):
    '''
    Esta funcion recibe la lista de letras y te devuelve otra lista de 10 letras elegidas
    pseudo-aleatoriamente (ignorar el pseudo en la expresion anterior) 
    La lista esta ordenada alfabeticamente
    '''
    resultado = []
    CANT_LETRAS = 10

    for i in range (CANT_LETRAS):
        posicion_aleatoria = random.randint(0,len(letras) - 1)
        resultado.append(letras[posicion_aleatoria])
        letras.pop(posicion_aleatoria)
    
    resultado.sort()
    return resultado

def ObtenerPalabras(diccionario,letras):
    '''
    ESTA FUNCION RECIBE DICCIONARIO DE PALABRA: DEFINICION y la lista del total de letras del rosco.
    Devuelve una lista ordenada alfabeticamente con las palabras elegidas
    '''
    resultado = []

    # Ordenar alfabeticamente las palabras y las letras facilita el procesamiento
    # 
    palabras = sorted(dicc.keys())
    palabras_a_usar = []
    
    for letra in letras:
        # AGREGAR PALABRAS QUE EMPIEZAN CON LA LETRA A OTRA LISTA
        PRIMER_LETRA = 0
        i = 0
        while letra == palabras[i][PRIMER_LETRA]:
            palabras_a_usar.append(palabras[i])
            i += 1

            if letra in ('a','e','i','o','u'):
                for palabra in ObtenerPalabrasAcentuadas(letra,palabras):
                    palabras_a_usar.append(palabra)

            # AGREGAR PALABRA A RESULTADO FINAL ALEATORIAMENTE
            resultado.append(palabras_a_usar[random.randint(0,len(palabras_a_usar) - 1)])
            
            # PARA FACILITAR FUTURAS BUSQUEDAS, ELIMINAR LLAVES UTILIZADAS
            for palabra in palabras_a_usar:
                palabras.remove(palabra)

            # VACIAR LAS PALABRAS UTILIZADAS
            palabras_a_usar.clear()

    return resultado

def ObtenerPalabrasAcentuadas(letra,palabras):
    # INICIAMOS LA BUSQUEDA DESDE EL FINAL DEBIDO A QUE sort() DEJA PALABRAS CON INICIO ACENTUADO AL FINAL DE LA LISTA
    resultado = []
    i = len(palabras) - 1
    while palabras[i] in ('á','é','í','ó','ú'):
        if letra == 'a' and palabras[i][0] == 'á':
            resultado.append(palabras[i])
        elif letra == 'e' and palabras[i][0] == 'é':
            resultado.append(palabras[i])
        elif letra == 'i' and palabras[i][0] == 'í':
            resultado.append(palabras[i])
        elif letra == 'o' and palabras[i][0] == 'ó':
            resultado.append(palabras[i])
        elif letra == 'u' and palabras[i][0] == 'ú':
            resultado.append(palabras[i])

        i -= 1

    return resultado

dicc = {'cantimpalo': 'es un fiambre', 'boca': 'el mas grande', 'slytherin': 'de putos'}
abc = sorted(string.ascii_lowercase)
lista = ObtenerLetras(abc)
palabras = ObtenerPalabras(dicc, lista)
print(palabras)