import doctest
def validar_contrasenia(contrasenia):
    """
    valida contraseñas
    >>> validar_contrasenia("!Algoritmos123")
    True
    >>> validar_contrasenia("!Algoritmos123!Algoritmos123")
    False
    >>> validar_contrasenia("algoritmos")
    False
    >>> validar_contrasenia("!Alg123")
    False
    >>> validar_contrasenia("algoritmos123")
    False
    """
    validar = False
    i = 0
    contarmay = 0
    contarmin = 0
    contarcarc = 0
    contarnum = 0
    while i < len(contrasenia) and validar == False and len(contrasenia) > 7 and len(contrasenia) < 15:
            if contrasenia[i].isupper() == True:
                contarmay +=1
            elif contrasenia[i].isalpha() == False and contrasenia[i].isnumeric() == False:
                contarcarc += 1
            elif contrasenia[i].isnumeric() == True:
                contarnum += 1
            elif contrasenia[i].isalpha() == True:
                contarmin += 1
            if contarmay > 0 and contarcarc > 0 and contarmin >0 and contarnum > 0:
             validar = True  
            i+=1
      
    return validar

doctest.testmod()
