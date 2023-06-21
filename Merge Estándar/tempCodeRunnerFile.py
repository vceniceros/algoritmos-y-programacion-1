########################## Mezcla de Archivos #############################
# Genera un unico archivo, en base a otros dos archivos de igual estructura
# y que estan ordenados por alguno de sus datos
# Cuando se encuentran dos "registros" con igual clave de comparacion,
# ambos registros se pasan al nuevo archivo.
# Se utiliza la misma funcion de lectura para ambos archivos
def leer_Archivo(archivo):
    linea = archivo.readline()
    return linea.rstrip('\n').split(',') if linea else ("","") #Devuelve 2 vacios

def grabar_Nuevo(archivo, codigoProducto, cantidadVendida):
    archivo.write(codigoProducto + ',' + cantidadVendida + '\n')

def mezclarArchivos(arSuc1, arSuc2, arSucGral):
    # Tener en cuenta que en esta funcion estamos recibiendo los archivos
    # abiertos, si no estuvieramos seguros que nos encontramos al principio
    # de los archivos, antes de hacer la primer lectura, deberiamos aplicar
    # un seek(0), a arSuc1 y arSuc2, para asegurar que procesaremos los datos
    # desde el principio al final de cada archivo
    codProdS1,cantS1 = leer_Archivo(arSuc1)
    codProdS2,cantS2 = leer_Archivo(arSuc2)
    while (codProdS1 and codProdS2):
        if (codProdS1 == codProdS2):
            grabar_Nuevo(arSucGral,codProdS1,cantS1)
            grabar_Nuevo(arSucGral,codProdS2,cantS2)
            codProdS1,cantS1 = leer_Archivo(arSuc1)
            codProdS2,cantS2 = leer_Archivo(arSuc2)
        elif (codProdS1 < codProdS2):
            grabar_Nuevo(arSucGral,codProdS1,cantS1)
            codProdS1,cantS1 = leer_Archivo(arSuc1)
        else: # codProdS1 > codProdS2
            grabar_Nuevo(arSucGral,codProdS2,cantS2)
            codProdS2,cantS2 = leer_Archivo(arSuc2)

    while codProdS1:
        grabar_Nuevo(arSucGral,codProdS1,cantS1)
        codProdS1,cantS1 = leer_Archivo(arSuc1)
    while codProdS2:
        grabar_Nuevo(arSucGral,codProdS2,cantS2)
        codProdS2,cantS2 = leer_Archivo(arSuc2)

#########################################################################

arSuc1 = open("sucursal1.csv","r")
arSuc2 = open("sucursal2.csv","r")
arSucGral = open("sucVentas.csv","w")
mezclarArchivos(arSuc1, arSuc2, arSucGral)
arSuc1.close()
arSuc2.close()
arSucGral.close()