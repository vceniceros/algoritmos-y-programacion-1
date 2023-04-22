def validar_contrasenia(password):
    """   
  >>> validar_contraseña("!Algoritmos123") 
  True
  >>>validar_contraseña("!Algoritmos123!Algoritmos123") 
  False
   >>>validar_contraseña("algoritmos")
   False
   >>>validar_contraseña("algoritmos123") 
   False
   >>>alidar_contraseña("Algoritmos123")
   False
   >>>validar_contraseña("!Alg123") 
   False
   
   """
    validar = True
    i = 0
    while i < len(password) and validar == True:
        if len(password) < 7 or len(password) > 15:
            validar = False
        elif password.isalpha == False:
            validar == False
        elif password.isnumeric == False:
            validar == False
        elif password.isupper == False:
            validar == False
        elif password.isalpha[i] == False and password.isnumeric[i] == False:
            validar == True
        i+=1
    return validar
    import doctest 
    print(doctest.testmod())
