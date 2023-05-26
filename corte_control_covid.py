""" Corte de control: DOS CORTES """
"""
    * El formato del archivo de ventas es:
    * CSV: fecha, vendedor, monto
    * Ordenado de menor a mayor por fecha y luego por vendedor
    *
    * Primer corte (mas interno) por vendedor
    * Segundo corte (mas externo) por dia
"""

# constantes 
MAX_DIA = 999999999999
MAX_REG = str(MAX_DIA) + ",xxx,xxx,0"
ARCHIVO = "casos_covid.csv"
DIA = 0
PAIS = 1
CASOS = 3

# funciones ====================================================

"""
    * funcion leer archivo - lee una línea del archivo
    *
    * pre: f es un archivo abierto con lineas con formato valido
    *
    * post: devuelve la línea como una lista de 3 valores
    *       dia, cliente, valor
    *       si llegó al fin de archivo devuelve MAX_REG
"""
def leer(archivo):
    linea = archivo.readline()
    if (not(linea)):
        linea = MAX_REG
    linea = linea.rstrip()
    return linea.split(',')

#---------------------------------------------------------------------

"""
    * funcion que recibe un registro y devuelve el dia y el valor
    *
    * pre: recibe un registro valido con tres campos
    *
    * post: pasa el valor a entero
    *       devuelve el dia de la operacion y el monto
"""
def dia_casos_valor(registro):
    casos = int(registro[CASOS])
    return registro[DIA], registro[PAIS], casos

#---------------------------------------------------------------------

"""
    * Funcion omprimir
    *
    * pre: leyenda y dato valido, booleana False por defecto
    *
    * post: imprime la leyenda con el dato que se pase
    *       si la booleana es True imprime una separacion con espacio
"""
def imprimir(leyenda, dato, separador = False):
    print(leyenda, dato)
    if (separador):
        guion = "=" * 55
        print (guion,'\n')
        
#---------------------------------------------------------------------

"""
    * total por cliente
    *
    * pre: recibe un registro valido y un archivo abierto
    *
    * post: acumula y devuelve el total por vendedor, el vendedor y el registro actual
"""
def total_pais(registro, archivo):
    dia, pais, casos        = dia_casos_valor(registro)
    dia_actual, pais_actual = dia, pais
    acumulado_pais = 0
    while (pais == pais_actual and dia == dia_actual and int(dia) < MAX_DIA):
        acumulado_pais  += casos
        registro        = leer(archivo)
        dia, pais, casos   = dia_casos_valor(registro)
        
    return acumulado_pais, pais_actual, registro

#---------------------------------------------------------------------

"""
    * total por dia
    *
    * pre: recibe un registro valido y un archivo abierto
    *
    * post: acumula y devuelve el total por dia y el registro actual
"""
""""""
def total_dia(registro, archivo):
    dia, pais, casos = dia_casos_valor(registro)
    dia_actual = dia
    pais_actual = pais
    acumulado_dia   = 0
    while (dia == dia_actual and int(dia) < MAX_DIA):
        acumulado_pais, pais_procesado, registro = total_pais(registro, archivo)
        leyenda = "   --- Acumulado por pais: " + pais_procesado 
        imprimir(leyenda, acumulado_pais)
        acumulado_dia  += acumulado_pais
        dia = registro[DIA]
        
    return acumulado_dia, registro

#---------------------------------------------------------------------

"""
    * funcion que hace el corte de control global
    *
    * pre: recibe un archivo bien formado, abierto
    *
    * post: genera e imprime por pantalla el corte de control
"""
def corte_control(archivo):
    # Leo cada una de las lineas
    registro = leer(archivo)
    acumulado_total = 0

    while (int(registro[DIA]) < MAX_DIA ):
        imprimir("\nTotal del dia", registro[DIA])
        acumulado_dia, registro = total_dia(registro, archivo)
        acumulado_total += acumulado_dia
        imprimir("  Acumulado por día", acumulado_dia, True)

    imprimir("\n====== Acumulado total =", acumulado_total)
    


#### =================================================

"""
    * funcion main
"""
def main():
    # Abro archivo para lectura
    archivo = open(ARCHIVO,'r')
    corte_control(archivo)
    archivo.close()

    
main()

