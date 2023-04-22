aux = 0
aux1 = 1
promedio = 0
nota = 1
while nota != 0:
    nota = int(input("Ingrese nota o 0 para terminar: "))
    aux = aux+nota
    aux1 = aux1+1
    promedio = aux/aux1
print(promedio)
