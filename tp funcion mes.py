
def nombreDelMes(mes):
    """devuelve el mes"""

    if mes == 1:
        mes = "Enero"
    elif mes == 2:
        mes =="Febrero"
    elif mes == 3:
        mes = "Marzo"
    elif mes == 4:
        mes = "Abril"
    elif mes == 5:
        mes = "Mayo"
    elif mes == 6:
        mes = "Junio"
    elif mes == 7:
        mes = "Julio"
    elif mes == 8:
        mes = "Agosto"
    elif mes == 9:
        mes = "Septiembre"
    elif mes == 10:
        mes = "Octubre"
    elif mes == 11:
        mes = "Noviembre"
    elif mes == 12:
        mes = "Diciembre"
    else:
        print("mes invalido")
        
    return mes
mes = int(input("ingrese mes: "))
print(nombreDelMes(mes))
