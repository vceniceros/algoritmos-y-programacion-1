def es_primo(numero):
    #tu codigo
     """valora si es primo"""
     es_primo = True 
     if numero <= 1:
         es_primo = False
     for i in range(2,numero): 
         if numero % i==0:
            es_primo= False
     return es_primo
def mayor_distancia_entre_primos(inferior, superior):
    """encuentra la distancia de numeros primos en un rango"""
    distacia = -1
    numero_primo_superior = None
    for i in range(inferior,superior+1):
        if es_primo(i):
            if numero_primo_superior is None:
             distacia = 0
            else:
                auxiliar = i-numero_primo_superior
                if auxiliar > distacia:
                    distacia = auxiliar
            numero_primo_superior=i
    return distacia
            

print(mayor_distancia_entre_primos(3,7))
