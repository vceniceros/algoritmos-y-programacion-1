def es_par(numero):
    if numero % 2 == 0:
        devolver = True
    else:
        devolver = False
    return devolver
print("es par" if(es_par(8)) else "es inpar")
print("es par" if(es_par(9)) else "es inpar")
