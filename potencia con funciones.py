def potencia(a,b):
    """potencia"""
    potenciacion= 1
    b = b+1
    while b > 0:
        potenciacion= a*a
        b= b-1
    return potenciacion

base = int(input("Ingrese la base: "))
potenciar = int(input("Ingrese la potencia: "))
print(potencia(base,potenciar))
import doctest
