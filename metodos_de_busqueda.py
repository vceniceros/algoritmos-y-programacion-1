import time
import random

MAX = 10000000

def busqueda(lista, valor):
    
    posicion = -1
    i = 0 
    while posicion == -1 and i < len(lista) and lista[i] <= valor:
        if lista[i] == valor:
           posicion = i
        else: 
            i = i + 1
    return posicion 
    


# codigo de busqueda binaria
def bus_bin(lista, valor):
    inf = 0
    sup = (len(lista)-1)
    posicion = -1

    while(posicion == -1) and (inf <= sup):
        medio = (inf + sup) // 2
        if(lista[medio] == valor):
            posicion = medio
        elif(lista[medio] < valor):
            inf = medio + 1
        else:
            sup = medio - 1
    return posicion

def lista_ran():
    l = []
    for i in range(MAX):
        l.append(random.randint(-MAX, MAX))
    return l

def main():
    lista1 = lista_ran()
    lista1.sort()
    ti1 = time.time()
    posicion1 = busqueda(lista1, 10)
    tf1 = time.time()
    t1 = tf1-ti1
    
    lista2 = lista_ran()
    lista2.sort()
    ti2 = time.time()
    posicion2 = bus_bin(lista2, 10)
    tf2 = time.time()
    t2 = tf2-ti2
    
    
    print("busqueda tomo :", t1)
    print("posicion: ", posicion1)
    
    
    print("bus bin tomo :", t2)
    print("posicion: ", posicion2)
    
    
main()