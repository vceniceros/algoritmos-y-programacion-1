# Escribir un programa que solicite el ingreso de números, y a medida que se ingresan, 
# calcule e informe el factorial de cada número.
# Para saber si el programa debe seguir solicitando ingresos, 
# se le debe preguntar al usuario si desea ingresar otro número.
# En caso que no se pueda calcular el factorial del número ingresado, 
# se debe informar que no es posible calcular el factorial para dicho número.
numero = 1
while numero != 0:
    numero = int(input("inserte numero, en caso de querer terminar ingrese 0: "))
    factorial = 1

    if numero > 0:
        for i in range(1, numero+1):
            factorial = factorial*i
    else: print("no se puede calcular ese factorial")
    print("factorial: ", factorial)
    
