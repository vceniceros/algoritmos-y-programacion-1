res_2014 = open("resultados_2014.txt","r",encoding='utf8')
res_2018 = open("resultados_2018.txt","r",encoding='utf8')
res_2022 = open("resultados_2022.txt","r",encoding='utf8')
def abrir_resultado():
    try:
        resultado = open('resultados.txt','r+',encoding='utf8')
    except:
        resultado = open('resultados.txt','w',encoding='utf8')
        resultado.close()
        resultado = open('resultados.txt','r+',encoding='utf8')
    return resultado
resultados = abrir_resultado()
MAX_DIA = '999'
FIN_ARCHIVO = MAX_DIA+",,,,"
año_2014 = '2014'
año_2018 = '2018'
año_2022 = '2022'
DIA = 0
LOCAL = 1
GOLES_LOCAL = 2
VISITANTE = 3
GOLES_VISTANTE = 4
ULTIMA_LINEA = ['','','','','']

def leer_Archivo(archivo):
    linea = archivo.readline()
    return linea.rstrip('\n').split(',') if linea else FIN_ARCHIVO.split(',')

def grabar_Nuevo(archivo, dia, local, local_gol, visitante, visitante_gol, año):
    archivo.write(dia + ',' + local + ',' + local_gol + ','+ visitante + ',' + visitante_gol + ',' + año + '\n')

def mezclarArchivos(res_2014, res_2018, res_2022, resultados):
    
    dia_2014, local_2014, local_gol_2014, visitante_2014, visitante_gol_2014 = leer_Archivo(res_2014)
    dia_2018, local_2018, local_gol_2018, visitante_2018, visitante_gol_2018 = leer_Archivo(res_2018)   
    dia_2022, local_2022, local_gol_2022, visitante_2022, visitante_gol_2022 = leer_Archivo(res_2022)
    
    while (int(dia_2014) < int(MAX_DIA) or int(dia_2018) < int(MAX_DIA) or int(dia_2022) < int(MAX_DIA)):
        dia_min = min(int(dia_2014),int(dia_2018),int(dia_2022))
        while int(dia_2014) == dia_min:
            grabar_Nuevo(resultados,dia_2014,local_2014, local_gol_2014, visitante_2014, visitante_gol_2014, año_2014)
            dia_2014, local_2014, local_gol_2014, visitante_2014, visitante_gol_2014 = leer_Archivo(res_2014)
        while int(dia_2018) == dia_min:    
            grabar_Nuevo(resultados,dia_2018,local_2018, local_gol_2018, visitante_2018, visitante_gol_2018, año_2018)
            dia_2018, local_2018, local_gol_2018, visitante_2018, visitante_gol_2018 = leer_Archivo(res_2018)
        while int(dia_2022) == dia_min:
            grabar_Nuevo(resultados,dia_2022, local_2022, local_gol_2022, visitante_2022, visitante_gol_2022, año_2022)
            dia_2022, local_2022, local_gol_2022, visitante_2022, visitante_gol_2022 = leer_Archivo(res_2022)
        


mezclarArchivos(res_2014, res_2018, res_2022 ,resultados)
res_2014.close()
res_2018.close()
res_2022.close()
resultados.seek(0)

def dic_victorias(equipo, dicc):
    """
    recibe un equipo y un diccionario y  devuelve un diccionario con el equipo como clave y sus victorias como valor
    """
    if equipo in dicc:
        dicc[equipo] +=1
    else:
        dicc[equipo] = 1

def dic_resultados(archivo):
    """
    recibe un archivo y devuelve un diccionario con pais como clave y partidos ganados como valor
    """
    dicc = {}
    linea = leer_Archivo(archivo)
    while int(linea[DIA]) < int(MAX_DIA):
        local = linea[LOCAL]
        visitante = linea[VISITANTE]
        goles_local = linea[GOLES_LOCAL]
        goles_visitante = linea[GOLES_VISTANTE]
        if goles_local > goles_visitante:
            dic_victorias(local, dicc)
        elif goles_visitante > goles_local:
            dic_victorias(visitante, dicc)
        linea = leer_Archivo(archivo)
    return dicc

def lista_dic(dicc):
    """
    recibe un diccionario y retorna una lista ordenda de mayor a menor
    """
    lista_ordenada = [(equipo, victorias) for equipo, victorias in dicc.items()]
    lista_ordenada = sorted(lista_ordenada,key= lambda x: x[1], reverse=True)
    return lista_ordenada

print(lista_dic(dic_resultados(resultados)))

