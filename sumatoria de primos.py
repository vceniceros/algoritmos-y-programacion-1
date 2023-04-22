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
def suma_de_numeros_primos(numero):
    """sumamos primos"""
    sumatoria = 0
    for i in range(0,numero+1):
        if es_primo(i) == True:
            sumatoria = sumatoria + i
    return sumatoria
            
    
print(suma_de_numeros_primos(-10))