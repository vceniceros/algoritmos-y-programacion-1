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
def escribir_nota(nota,texto):
     """
     Se desea escribir una nota de rescate recortando letras de una revista.
     Escribir una función que reciba
     por parámetro la nota que se desea escribir y el texto completo de la revista, 
     y devuelva True si la revista contiene todas las letras necesarias para escribir la nota 
     (ignorando mayúsculas y minúsculas), False en caso contrario.

     Ejemplo: Si la revista contiene "Algoritmos y Programacion", podemos
     escribir la nota "Gracias por la moto", p
     ero no se puede escribir "Porotos amargos" (falta una s).
     >>> palabra = 'algoritmos y programacion'
     >>> nota_1 = 'Porotos amargos'
     >>> nota_2 = 'gracias por la moto'
     >>> escribir_nota(nota_1, palabra)
     False
     >>> escribir_nota(nota_2, palabra)
     False
     """
     dicc_nota = {}
     dicc_texto = {}
     resultado = False
     for i in range(len(nota)):
          if nota[i] not in dicc_nota and nota[i] != " ":
               dicc_nota[nota[i]]=1
          elif nota[i] != " ": 
               dicc_nota[nota[i]]+=1
     for i in range(len(texto)):
          if texto[i] not in dicc_texto and texto[i] != " ":
               dicc_texto[texto[i]]=1
          elif texto[i] != " ":
               dicc_texto[texto[i]]+=1
     cantidad_de_letras_nota = 0
     cantidad_de_letras_texto = 0
     for cantidad in dicc_nota.values():
          cantidad_de_letras_nota+=cantidad
     for cantidad in dicc_texto.values():
          cantidad_de_letras_texto+=cantidad
     claves_texto = [x for x in dicc_texto.keys()]
     for letras in dicc_nota.keys():
          acum_letras_de_nota_en_texto = 0
          if letras in claves_texto:
               acum_letras_de_nota_en_texto +=1
     if acum_letras_de_nota_en_texto == len(dicc_nota.keys()) and cantidad_de_letras_texto >= cantidad_de_letras_nota:
          resultado = True
     return resultado
def normalizar(letra):
     """
     >>> normalizar('á')
     'a'
     """
     letra_normalizada = ''
     if letra.isupper():
          letra_normalizada = letra.lower()
     elif letra == 'á':
          letra_normalizada = 'a'
     elif letra =='é':
          letra_normalizada ='e'
     elif letra == 'í':
          letra_normalizada = 'i'
     elif letra == 'ó':
          letra_normalizada = 'o'
     elif letra == 'ú':
          letra_normalizada = 'u'
     else:
          letra_normalizada = letra
     return letra_normalizada
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
          letra = normalizar(letra)
          if letra not in lista and letra.isalpha():
               lista.append(letra)
      return len(lista)
def elegir(actividad_por_ciudad, actividades_deseadas, precio_por_actividad,COSTO_MAXIMO = 20000,CANTIDAD_MINIMA_ACTIVIDADES = 3):
      """ 
      >>> lista_1 = ["museo","senderismo","bares","montañismo"]
     >>> lista_2 = ["bares","senderismo","museo","conciertos"]
     >>> lista_3 = ["museo","conciertos","bares"]
     >>> elegir(lista_1,lista_2, 5000)
     True
     >>> elegir(lista_1,lista_3, 1000)
     False
     >>> elegir(lista_1,lista_2, 10000)
     False
      """
      resultado = False
      actividades_de_ciudad_deseadas = 0
      for activad in actividad_por_ciudad:
           if activad in actividades_deseadas:
                actividades_de_ciudad_deseadas+=1
      if actividades_de_ciudad_deseadas >= CANTIDAD_MINIMA_ACTIVIDADES and actividades_de_ciudad_deseadas*precio_por_actividad <= COSTO_MAXIMO:
           resultado = True
      return resultado
def camino_a_la_fama_diccionario(lista):
     """
     >>> lista_1 = [["Juan",10],["Mariano",4],["Pepe",7],["Juan",8],["Mariano",7],["Pepe",9],["Juan",9],["Mariano",6],["Pepe",8]]
    >>> camino_a_la_fama_diccionario(lista_1) 
    {'Juan': [27, 3, 9], 'Mariano': [17, 3, 5], 'Pepe': [24, 3, 8]}
     """
     dicc = {}
     PARTICIPANTE = 0
     PUNTO = 1
     SUMA_PUNTOS=0
     CANTIDAD = 1
     PROMEDIO = 2
     for voto in lista:
          suma_puntos = voto[PUNTO]
          cantidad_votos = 1
          promedio = voto[PUNTO]
          if voto[PARTICIPANTE] not in dicc:
               dicc[voto[PARTICIPANTE]]=[suma_puntos,cantidad_votos,promedio]
          else:
               dicc[voto[PARTICIPANTE]][SUMA_PUNTOS]+=suma_puntos
               dicc[voto[PARTICIPANTE]][CANTIDAD]+=1
               dicc[voto[PARTICIPANTE]][PROMEDIO]=dicc[voto[PARTICIPANTE]][SUMA_PUNTOS]
               dicc[voto[PARTICIPANTE]][PROMEDIO]=dicc[voto[PARTICIPANTE]][PROMEDIO]/dicc[voto[PARTICIPANTE]][CANTIDAD]
               dicc[voto[PARTICIPANTE]][PROMEDIO]=int(dicc[voto[PARTICIPANTE]][PROMEDIO])
     return dicc     
def camino_a_la_fama(lista):
     """ 
      >>> lista_1 = [["Juan",10],["Mariano",4],["Pepe",7],["Juan",8],["Mariano",7],["Pepe",9],["Juan",9],["Mariano",6],["Pepe",8]]
      >>> camino_a_la_fama(lista_1)
      [('Juan', 9), ('Pepe', 8), ('Mariano', 5)]
     """
     PROM = 2
     PROM_L = 1
     dicc = camino_a_la_fama_diccionario(lista)
     lista = [(nombre, promedio[PROM]) for (nombre, promedio) in dicc.items()]
     lista.sort(key=lambda x:x[PROM_L],reverse=True)
     return lista
def validar(clave,MAX_LONG = 12,MIN_LONG = 8, CARAC = ['*', '-', '$', '@'],TILDES = ['á', 'é', 'í', 'ó', 'ú', 'Á', 'É', 'Í', 'Ó', 'Ú']):
     """
     >>> clave_1 = 'Algoritmo $1'
     >>> clave_2 = 'Aprobé-con-7'
     >>> clave_3 = 'Algoritmo$1'
     >>> clave_4 = 'Aprobe-con-7'
     >>> validar(clave_1)
     False
     >>> validar(clave_2)
     False
     >>> validar(clave_3)
     True
     >>> validar(clave_4)
     True
     """
     cont_may = cont_min = cont_num = cont_carac = cont_esp =  cont_tilde = cont_carac_inva= i = 0
     
     resultado = False
     while i < len(clave):
        if clave[i].isspace():
            cont_esp += 1
        elif clave[i] not in CARAC and not clave[i].isalpha() and not clave[i].isnumeric():
            cont_carac_inva += 1
        elif clave[i] in TILDES:
            cont_tilde += 1
        elif clave[i].isupper():
            cont_may += 1
        elif clave[i].islower():
            cont_min += 1
        elif clave[i].isnumeric():
            cont_num += 1
        elif clave[i] in CARAC:
            cont_carac += 1
        i += 1

     if cont_may >= 1 and cont_min >= 1 and cont_num >= 1 and cont_carac >= 1 and cont_carac_inva == 0 and cont_esp == 0 and cont_tilde == 0 and len(clave) >= MIN_LONG and len(clave) <= MAX_LONG:
        resultado = True
     return resultado
def elegir(lista_1,lista_2,cuota,PRESUPUESTO = 5000,CANTIDAD_MIN_ACTI = 3):
    """
    >>> lista_1 = ["natación", "gimnasio", "voley", "futbol"]
    >>> lista_2  = ["natación", "voley", "gimnasio"] 
    >>> lista_3 = ["natación", "futbol", "karate"]
    >>> elegir(lista_1, lista_2, 5000) 
    True
    >>> elegir(lista_2, lista_3,100)
    False
    >>> elegir(lista_2, lista_2,5500)
    False
    """
    actividades_similares = 0
    resultado = False
    for actividad in lista_1:
         if actividad in lista_2:
              actividades_similares +=1
    if actividades_similares >= CANTIDAD_MIN_ACTI and cuota <= PRESUPUESTO:
         resultado = True
    return resultado
def procesar_partidos(lista):
     """
     >>> lista_1 = [["PP", 19, 35], ["PSOE", 20, 30], ["VOX", 15, 15], ["PP", 0, 151],["PSOE", 20, 0],["VOX", 0, 11]]
     >>> procesar_partidos(lista_1)
     {'PP': 205, 'PSOE': 70, 'VOX': 41}
     """
     dicc = {}
     NOMBRE = 0
     DIPUTADOS = 1
     SENADORES = 2
     for partido in lista:
          if partido[NOMBRE] not in dicc:
               dicc[partido[NOMBRE]]=partido[DIPUTADOS]+partido[SENADORES]
          else:
               dicc[partido[NOMBRE]]+=partido[DIPUTADOS]+partido[SENADORES]
     return dicc
def ordenar_votos(lista):
     """
     >>> lista_1 = [["PP", 19, 35], ["PSOE", 20, 30], ["VOX", 15, 15], ["PP", 0, 151],["PSOE", 20, 0],["VOX", 0, 11]]
     >>> ordenar_votos(lista_1)
     [('PP', 205), ('PSOE', 70), ('VOX', 41)]
     """
     VOTOS =1
     dicc = procesar_partidos(lista)
     lista_ordenada = [x for x in dicc.items()]
     lista_ordenada.sort(reverse=True, key=lambda x:x[VOTOS])
     return lista_ordenada
def mayor_y_menor(lista):
     """
     >>> lista = [21, 4, 5, 6, 7, 15, 10, 3, 42, 2]
     >>> mayor_y_menor(lista)
     [2, 42]
     """
     max = 0
     min = 0
     max_min = []
     for numero in lista:
          min = numero
          if numero > max:
               max = numero
          elif numero < min:
               min = numero
     max_min.append(min)
     max_min.append(max)
     return max_min
def contar_letra_en_texto(texto):
     """
     >>> palabra = 'Hola mundo'
     >>> contar_letra_en_texto(palabra)
     {'H': 1, 'o': 2, 'l': 1, 'a': 1, ' ': 1, 'm': 1, 'u': 1, 'n': 1, 'd': 1}
     """
     dicc = {}
     for letra in range(len(texto)):
          if texto[letra] not in dicc:
               dicc[texto[letra]]=1
          else:
               dicc[texto[letra]]=texto.count(texto[letra])
     return dicc
def pedir_votos():
     continuar = 's'
     lista = []
     while continuar != 'n':
          partido = input("Ingrese el partido a sumarle votos: ")
          voto = int(input("Ingrese la cantidad de votos a sumarle:"))
          lista.append((partido, voto))
          continuar = input("Desea seguir ingresando?(s/n): ")
          if continuar !='s' and continuar !='n':
               continuar = input("tecla equivocada, desea continuar con la votacion?: ")
     return lista
def procesar_votos(PARTIDO = 0, VOTO = 1):
     lista = pedir_votos()
     dicc = {}
     
     for voto in lista:
          if voto[PARTIDO] not in dicc:
               dicc[voto[PARTIDO]]=voto[VOTO]
          else:
               dicc[voto[PARTIDO]]+=voto[VOTO]
     return dicc
def ordernar_votos_nuevos(VOTO = 1):
     dicc = procesar_votos()
     lista = [x for x in dicc.items()]
     lista.sort(reverse=True,key= lambda x:x[VOTO])
     return lista
def main(PARTIDO = 0,VOTOS = 1):
     lista = ordernar_votos_nuevos()
     cadena = ''
     for votos in lista:
          cadena += 'El partido {} obtuvo {} votos.\n'.format(votos[PARTIDO],votos[VOTOS])
     return print(cadena)
main()
doctest.testmod() 