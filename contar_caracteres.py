def validar_contrasenia(contrasenia):
    """
    >>>   validar_contraseña("!Algoritmos123")
    True
    """
    validar = False
    i = 0
    while i < len(contrasenia):
        if contrasenia.isalpha() == True and contrasenia.isnumeric() == True and contrasenia.isupper()==True and len(contrasenia)>7 and len(contrasenia) < 15 :
            validar = True
          i+=1
    return validar

import doctest
doctest.testmod()
