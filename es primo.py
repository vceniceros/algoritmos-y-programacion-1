def es_primo(numero):
    #tu codigo
     es_primo = True 
     if numero <= 1:
         es_primo = False
     for i in range(2,numero): 
         if numero % i==0:
            es_primo= False
     return es_primo

n = int(input("Ingrese numero: "))
print(es_primo(n))