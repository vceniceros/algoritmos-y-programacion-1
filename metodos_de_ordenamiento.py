#seleccion : es una bosta, agarra al mas chico , lo lleva adelante y va por el siguiente numero hasta encontrar uno mas chico y repetir
#burbujeo, hace lo mismo pero mas local, este por pasada hace mas intercambios 
#insercion: es el mas eficiente, 
# inserta un numero a la lista,
# lista esta ordenada porque hay un unico elemento, 
# inserto otro numero, si es mas chico va primero sino va segundo, 
# luego inserto otro, lo compara con el ultimo, 
# si es mas grande se queda sino se compara al anterior y asi 
#insercion: es excelente si la lista esta mas o menos ordenada y hayh que hacer pocas comparaciones
import random
import time
MAX = 10000

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


def seleccion(lista):
    n = len(lista)
    for i in range(n - 1):
        pos_min = i
        for j in range(i + 1, n):
            if (lista[j] < lista[pos_min]):
                pos_min = j

        intercambiar(lista, i, pos_min)

def insercion(lista):
    n = len(lista)
    for i in range(1, n):
        auxiliar = lista[i]
        j = i
        while ((j > 0) and (lista[j - 1] > auxiliar)):
            lista[j] = lista[j - 1]
            j = j - 1
        lista[j] = auxiliar
        
    


def main():

   l = []
   l1 = []
   l2 = []
   l3 = []
   for i in range(MAX):
        l1.append(random.randint(-MAX, MAX))
   for i in range(MAX):
        l2.append(random.randint(-MAX, MAX))
   for i in range(MAX):
        l3.append(random.randint(-MAX, MAX))
   
   ti1 = time.time()
   insercion(l1)
   print(l1)
   tf1 = time.time()
   t1 = tf1-ti1
   
   ti2 = time.time()
   seleccion(l2)
   print(l2)
   tf2 = time.time()
   t2 = tf2-ti2
   
   ti3 = time.time()
   burbujeo(l3)
   tf3 = time.time()
   t3 = tf3-ti3
   
   print("insercion tomo: ",t1)
   print("seleccion tomo: ",t2)
   print("burbujeo: ",t3)
   # print("Termine de ordenar")


main()