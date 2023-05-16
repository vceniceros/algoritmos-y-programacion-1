from datos import obtener_lista_definiciones

def palabras_candidatas(obtener_lista_definiciones):
    """ 
    Palabras_candidataas toma los datos de la funcion dada y crea un diccionario con 
    aquellos strings que complan con la condicion. condicion: el largo de la palabra tiene 
    que ser igual o mayor a 5.

    """

    diccionario={}
    minimo_de_letras=5

    for indice in obtener_lista_definiciones:

        if len(indice[0])>=minimo_de_letras:

            diccionario[indice[0]]=indice[1]

    return diccionario

def cantidad_de_palabras(palabras_candidatas):
    """
    Esta otra funcion toma aquellas palabras candidatas y muestra cuantas palabras inician con esa letra 
    del abcedario. Ademas nos muestra la cantidad total de palabras totales que hay. (eso me falta)
    
    """
    
    lista_abecedario=["a","b","c", "d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
    
    diccionario_solo_de_letras_y_cantidad={}
    lista_de_palabras=[]

    for indice in palabras_candidatas:

        lista_de_palabras.append(indice[0])
    

    for letra in lista_abecedario:


        if letra=="a":
            diccionario_solo_de_letras_y_cantidad[letra]= lista_de_palabras.count("a")
        
        elif letra=="b":
            diccionario_solo_de_letras_y_cantidad[letra]= lista_de_palabras.count("b")

        elif letra=="c":
            diccionario_solo_de_letras_y_cantidad[letra]= lista_de_palabras.count("c")

        elif letra=="d":
            diccionario_solo_de_letras_y_cantidad[letra]= lista_de_palabras.count("d")

        elif letra=="e":
            diccionario_solo_de_letras_y_cantidad[letra]= lista_de_palabras.count("e")

        elif letra=="f":
            diccionario_solo_de_letras_y_cantidad[letra]= lista_de_palabras.count("f")

        elif letra=="g":
            diccionario_solo_de_letras_y_cantidad[letra]= lista_de_palabras.count("g")

        elif letra=="h":
            diccionario_solo_de_letras_y_cantidad[letra]= lista_de_palabras.count("h")

        elif letra=="i":
            diccionario_solo_de_letras_y_cantidad[letra]= lista_de_palabras.count("i")

        elif letra=="j":
            diccionario_solo_de_letras_y_cantidad[letra]= lista_de_palabras.count("j")

        elif letra=="k":
            diccionario_solo_de_letras_y_cantidad[letra]= lista_de_palabras.count("k")

        elif letra=="l":
            diccionario_solo_de_letras_y_cantidad[letra]= lista_de_palabras.count("l")

        elif letra=="m":
            diccionario_solo_de_letras_y_cantidad[letra]= lista_de_palabras.count("m")

        elif letra=="n":
            diccionario_solo_de_letras_y_cantidad[letra]= lista_de_palabras.count("n")

        elif letra=="ñ":
            diccionario_solo_de_letras_y_cantidad[letra]= lista_de_palabras.count("ñ")

        elif letra=="o":
            diccionario_solo_de_letras_y_cantidad[letra]= lista_de_palabras.count("o")

        elif letra=="p":
            diccionario_solo_de_letras_y_cantidad[letra]= lista_de_palabras.count("p")

        elif letra=="q":
            diccionario_solo_de_letras_y_cantidad[letra]= lista_de_palabras.count("q")

        elif letra=="r":
            diccionario_solo_de_letras_y_cantidad[letra]= lista_de_palabras.count("r")

        elif letra=="s":
            diccionario_solo_de_letras_y_cantidad[letra]= lista_de_palabras.count("s")

        elif letra=="t":
            diccionario_solo_de_letras_y_cantidad[letra]= lista_de_palabras.count("t")

        elif letra=="u":
            diccionario_solo_de_letras_y_cantidad[letra]= lista_de_palabras.count("u")
    
        elif letra=="v":
            diccionario_solo_de_letras_y_cantidad[letra]= lista_de_palabras.count("v")

        elif letra=="w":
            diccionario_solo_de_letras_y_cantidad[letra]= lista_de_palabras.count("w")

        elif letra=="x":
            diccionario_solo_de_letras_y_cantidad[letra]= lista_de_palabras.count("x")

        elif letra=="y":
            diccionario_solo_de_letras_y_cantidad[letra]= lista_de_palabras.count("y")

        elif letra=="z":
            diccionario_solo_de_letras_y_cantidad[letra]= lista_de_palabras.count("z")


    return diccionario_solo_de_letras_y_cantidad

print("El total de palabras que hay por cada letra es: ", cantidad_de_palabras(palabras_candidatas(obtener_lista_definiciones())), "La cantidad de palabras totales que hay en el diccionario es de: ")









