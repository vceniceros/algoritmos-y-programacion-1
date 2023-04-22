def suma_de_divisores(numero):
    """suma todos los divisores de un numero"""
    divisores = 0
    for i in range(1,numero):
        if numero%i == 0:
            divisor = numero/i
            divisores = divisores + divisor
         
    return divisores-numero
            
        
            
          
print(suma_de_divisores(7))