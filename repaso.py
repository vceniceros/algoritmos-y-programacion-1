import doctest
def validad_clave(clave):
    """ 
    >>> palabra1 = 'Jorgito123@'
    >>> palabra2 = 'hola'
    >>> palabra3 = 'Jorgito 123'
    >>> validad_clave(palabra1)
    True
    >>> validad_clave(palabra2)
    False
    >>> validad_clave(palabra3)
    False
    """
    MAX_LENGHT = 16
    MIN_LENGHT = 8
    cont_min = cont_may =  cont_esp = cont_especiales = 0
    SIMBOLO = ['*','#','@','!']
    resultado = False
    if len(clave) >= MIN_LENGHT and len(clave) <= MAX_LENGHT:
        i = 0
        while cont_esp == 0 and i < len(clave):
            if clave[i] in SIMBOLO:
                cont_especiales += 1
            elif clave[i].isupper():
                cont_may+=1
            elif clave[i].islower():
                cont_min +=1
            elif clave[i] == " ":
                cont_esp += 1
            i+=1
        if cont_may>= 1 and cont_min>=1 and cont_especiales>=1 and cont_esp == 0:
            resultado = True
    return resultado
mesas1 = {"mesa_1": [("peter norton",'201'),("steve jobs",'600'),("bill gates",'59999'),("larry Elisson",'400'),("Elon musk",'80000')]}
#imprimir el total de electores por mesa (total1,total2,...totaln)
#imprimir el total de votos por forma decrecioente
def cargar_estructura(mesas):
    lista_mesas = []
    votos= {}
    CANDIDATO = 0
    VOTO_CANDIDATO = 1
    for mesa in mesas.values():
        acum = 0
        for voto in mesa:
            acum+=int(voto[VOTO_CANDIDATO])
            if voto[CANDIDATO] in votos.keys():
                votos[voto[CANDIDATO]] += int(voto[VOTO_CANDIDATO])
            else:
                votos[voto[CANDIDATO]] = int(voto[VOTO_CANDIDATO])
        lista_mesas.append(acum)
    print(lista_mesas)
    print(sorted(votos.items(),key=lambda x:x[1],reverse =True))
    
cargar_estructura(mesas1)
doctest.testmod()

        