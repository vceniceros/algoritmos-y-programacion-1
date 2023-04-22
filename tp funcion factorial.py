numero = 0
factorial = 1
def calcularFactorial(numero):
    """devuelve un factorial"""
    if numero > 0:
        for i in range(1, numero+1):
          numero = numero*i
    else:
        factorial = "numero invalido"
    return numero
print(calcularFactorial(3),calcularFactorial(5),calcularFactorial(-1))
