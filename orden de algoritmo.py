#operaciones elementales
import time 
N = 1000000
x = 0#1 OE 
ti = time.time()
while x < N: #1 OE
    x = x + 1 #2 OE
 #2 OE + 3OE * N 
tf = time.time()
t = tf-ti
print("la operacion tomo:", t)
print("en un segundo salen: ", int(3*N / t))
# sabiendo cuantas operaciones 
# elementales hace una maquina podemos ver en cuanto tiempo ejecuta nuesto algoritmo
#O = orden de algoritmo: cantidad de operaciones que hace tu algoritmo 
#O(3000002)
#O(3000002 * 1)
#3000002 * O(1)
#O(1) = orden constante 
#O(3N)+O(3)= 3 * O(n) + O(1) O(1) es despreciable ,3 tambien, queda O(N)