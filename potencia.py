base = int(input("Ingrese la base: "))
potencia = int(input("Ingrese la potencia: "))
potencia = potencia+1
while potencia > 0:
    potenciacion=base*base
    potencia= potencia-1

print(potenciacion)
