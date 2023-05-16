def intercambiar(l, i, j):
    aux = l[i]
    l[i] = l[j]
    l[j] = aux
    
def burbujeo(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(1, n - i):
            if (lista[j - 1] > lista[j]):
                intercambiar(lista, j-1, j)
def burbujeo_inverso(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(1, n - i):
            if (lista[j - 1] < lista[j]):
                intercambiar(lista, j-1, j)

def ordenar(lista, sentido):
    if sentido == 1:
        burbujeo(lista)
    elif sentido ==2:
        burbujeo_inverso(lista)
    return lista

Lista = [11, 2, 16, 8]
print(ordenar(Lista, 1))
print(ordenar(Lista, 2))

