def open_resultado():
    try:
        resultados = open('resultados.txt', 'r+')
    except:
        resultados = open('resultados.txt', 'w')
        resultados.close()
        resultados = open('resultados.txt', 'r+')
    return resultados

MAX_DIA = '99'
FIN_ARCHIVO = MAX_DIA+',,,,'
FIN_ARCHIVO_NEW =  MAX_DIA+',,,,,'
AÑO_14 = '2014'
AÑO_18 = '2018'
AÑO_22 = '2022'

resultados_2014 = open('resultados_2014.txt', 'r+',encoding='utf8')
resultados_2018 = open('resultados_2018.txt', 'r+',encoding='utf8')
resultados_2022 = open('resultados_2022.txt', 'r+',encoding='utf8')
resultados = open_resultado()

def read_Line_resultados(archive):
    line = archive.readline()
    return line.rstrip('\n').split(',') if line else FIN_ARCHIVO.split(',')

def read_Line_resultados_new(archive):
    line = archive.readline()
    return line.rstrip('\n').split(',') if line else FIN_ARCHIVO_NEW.split(',')

def write_resultados(archive, dia, local, gol_local, visitante, gol_visitante, año):
    archive.write(dia + ',' +  local + ',' + gol_local + ',' + visitante + ',' + gol_visitante + ',' + año + '\n')

def merge_resultados(resultados, resultados_2014, resultados_2018, resultados_2022):
    dia_14, local_14, local_gol_14, visitante_14, visitante_gol_14 = read_Line_resultados(resultados_2014)
    dia_18, local_18, local_gol_18, visitante_18, visitante_gol_18 = read_Line_resultados(resultados_2018)
    dia_22, local_22, local_gol_22, visitante_22, visitante_gol_22 = read_Line_resultados(resultados_2022)

    while int(dia_14) < int(MAX_DIA) or int(dia_18) < int(MAX_DIA) or int(dia_22) < int(MAX_DIA):
        min_dia = min(int(dia_14),int(dia_18), int(dia_22))
        while int(dia_14) == min_dia:
            write_resultados(resultados, dia_14, local_14, local_gol_14, visitante_14, visitante_gol_14, AÑO_14)
            dia_14, local_14, local_gol_14, visitante_14, visitante_gol_14 = read_Line_resultados(resultados_2014)
         
        while int(dia_18) == min_dia:
            write_resultados(resultados, dia_18, local_18, local_gol_18, visitante_18, visitante_gol_18, AÑO_18)
            dia_18, local_18, local_gol_18, visitante_18, visitante_gol_18 = read_Line_resultados(resultados_2018)

        while int(dia_22) == min_dia:
            write_resultados(resultados, dia_22, local_22, local_gol_22, visitante_22, visitante_gol_22, AÑO_22)
            dia_22, local_22, local_gol_22, visitante_22, visitante_gol_22 = read_Line_resultados(resultados_2022)

        dia_14, local_14, local_gol_14, visitante_14, visitante_gol_14 = read_Line_resultados(resultados_2014)
        dia_18, local_18, local_gol_18, visitante_18, visitante_gol_18 = read_Line_resultados(resultados_2018)
        dia_22, local_22, local_gol_22, visitante_22, visitante_gol_22 = read_Line_resultados(resultados_2022)

merge_resultados(resultados, resultados_2014, resultados_2018, resultados_2022)
resultados_2014.close()
resultados_2018.close()
resultados_2022.close()
resultados.seek(0)


def dicc_victorias_resultados(archive):
    dicc = {}
    dia, local, gol_local, visitante, gol_visitante, año = read_Line_resultados_new(resultados)
    while int(dia) < int(MAX_DIA):
        if gol_local > gol_visitante:
           if local in dicc:
               dicc[local] += 1
           else:
               dicc[local] = 1
        elif  gol_visitante > gol_local:
            if visitante in dicc:
               dicc[visitante] += 1
            else:
               dicc[visitante] = 1
        dia, local, gol_local, visitante, gol_visitante, año = read_Line_resultados_new(resultados)
    return dicc

def ordenar_lista(archivo):
    dicc = dicc_victorias_resultados(archivo)
    lista = sorted(dicc.items(), key=lambda x: x[1], reverse=True)
    return lista
    

print(ordenar_lista(resultados))
        
