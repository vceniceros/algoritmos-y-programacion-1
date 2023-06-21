########################## Mezcla de Archivos #############################
# Genera un unico archivo, en base a otros dos archivos de igual estructura
# y que estan ordenados por alguno de sus datos
# Cuando se encuentran dos "registros" con igual clave de comparacion,
# ambos registros se pasan al nuevo archivo.
# Se utiliza la misma funcion de lectura para ambos archivos


def leer_Archivo(archivo):
    linea = archivo.readline()
    return linea.rstrip('\n').split(',') if linea else ("","","","","") #Devuelve 2 vacios

def grabar_Nuevo(archivo, dia, local, local_gol, visitante, visitante_gol):
    archivo.write(dia + ',' + local + ',' + local_gol + ','+ visitante + ',' + visitante_gol + '\n')

def mezclarArchivos(res_2014, res_2018, res_2022, resultados):
    # Tener en cuenta que en esta funcion estamos recibiendo los archivos
    # abiertos, si no estuvieramos seguros que nos encontramos al principio
    # de los archivos, antes de hacer la primer lectura, deberiamos aplicar
    # un seek(0), a res_2014 y res_2018, para asegurar que procesaremos los datos
    # desde el principio al final de cada archivo
    dia_2014, local_2014, local_gol_2014, visitante_2014, visitante_gol_2014 = leer_Archivo(res_2014)
    dia_2018, local_2018, local_gol_2018, visitante_2018, visitante_gol_2018 = leer_Archivo(res_2018)
    dia_2022, local_2022, local_gol_2022, visitante_2022, visitante_gol_2022 = leer_Archivo(res_2022)
    while (dia_2014 and dia_2018 and dia_2022):
        if (dia_2014 == dia_2018 == dia_2022):
            grabar_Nuevo(resultados,dia_2014,local_2014, local_gol_2014, visitante_2014, visitante_gol_2014)
            grabar_Nuevo(resultados,dia_2018,local_2018, local_gol_2018, visitante_2018, visitante_gol_2018 )
            grabar_Nuevo(resultados,dia_2022, local_2022, local_gol_2022, visitante_2022, visitante_gol_2022)
            dia_2014, local_2014, local_gol_2014, visitante_2014, visitante_gol_2014 = leer_Archivo(res_2014)
            dia_2018, local_2018, local_gol_2018, visitante_2018, visitante_gol_2018 = leer_Archivo(res_2018)
            dia_2022, local_2022, local_gol_2022, visitante_2022, visitante_gol_2022 = leer_Archivo(res_2022)
        elif (dia_2014 < dia_2018 or dia_2014 < dia_2022):
            grabar_Nuevo(resultados,dia_2014,local_2014, local_gol_2014, visitante_2014, visitante_gol_2014)
            dia_2014, local_2014, local_gol_2014, visitante_2014, visitante_gol_2014 = leer_Archivo(res_2014)
        else: 
            grabar_Nuevo(resultados,dia_2018,local_2018, local_gol_2018, visitante_2018, visitante_gol_2018 )
            grabar_Nuevo(resultados,dia_2022, local_2022, local_gol_2022, visitante_2022, visitante_gol_2022)
            dia_2018, local_2018, local_gol_2018, visitante_2018, visitante_gol_2018 = leer_Archivo(res_2018)
            dia_2022, local_2022, local_gol_2022, visitante_2022, visitante_gol_2022 = leer_Archivo(res_2022)
    while dia_2014:
        grabar_Nuevo(resultados,dia_2014,local_2014, local_gol_2014, visitante_2014, visitante_gol_2014)
        dia_2014, local_2014, local_gol_2014, visitante_2014, visitante_gol_2014 = leer_Archivo(res_2014)
    while dia_2018:
        grabar_Nuevo(resultados,dia_2018,local_2018, local_gol_2018, visitante_2018, visitante_gol_2018 )
        dia_2018, local_2018, local_gol_2018, visitante_2018, visitante_gol_2018 = leer_Archivo(res_2018)
    while dia_2022:
        grabar_Nuevo(resultados,dia_2022,local_2022, local_gol_2022, visitante_2022, visitante_gol_2022 )
        dia_2022, local_2022, local_gol_2022, visitante_2022, visitante_gol_2022 = leer_Archivo(res_2022)
    
#########################################################################

res_2014 = open("resultados_2014.txt","r")
res_2018 = open("resultados_2018.txt","r")
res_2022 = open("resultados_2022.txt","r")
resultados = open("resultados.txt","w")
mezclarArchivos(res_2014, res_2018, res_2022 ,resultados)
res_2014.close()
res_2018.close()
res_2022.close()
resultados.close()
