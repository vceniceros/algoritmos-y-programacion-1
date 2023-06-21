########################## Mezcla de Archivos #############################
# Genera un unico archivo, en base a otros dos archivos de igual estructura
# y que estan ordenados por alguno de sus datos
# Cuando se encuentran dos "registros" con igual clave de comparacion,
# ambos registros se pasan al nuevo archivo.
# Se utiliza la misma funcion de lectura para ambos archivos
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

def leer_Archivo(archivo):
    linea = archivo.readline()
    return linea.rstrip('\n').split(',') if linea else FIN_ARCHIVO.split(',')

def grabar_Nuevo(archivo, dia, local, local_gol, visitante, visitante_gol, año):
    archivo.write(dia + ',' + local + ',' + local_gol + ','+ visitante + ',' + visitante_gol + ',' + año + '\n')

def mezclarArchivos(res_2014, res_2018, res_2022, resultados):
    # Tener en cuenta que en esta funcion estamos recibiendo los archivos
    # abiertos, si no estuvieramos seguros que nos encontramos al principio-
    # de los archivos, antes de hacer la primer lectura, deberiamos aplicar
    # un seek(0), a res_2014 y res_2018, para asegurar que procesaremos los datos
    # desde el principio al final de cada archivo
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
        
    
#########################################################################


mezclarArchivos(res_2014, res_2018, res_2022 ,resultados)
res_2014.close()
res_2018.close()
res_2022.close()
resultados.seek(0)

