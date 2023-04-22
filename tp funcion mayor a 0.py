def mayor_a_0(numero):
    """muestra si el numero es mayor de 0"""
    while numero <= 0:
       print("error: ingrese numero mayor a 0")
       numero = int(input("ingrese numero: "))
    return numero

numero = int(input("ingrese numero: "))
mayor_a_0(numero)

    
