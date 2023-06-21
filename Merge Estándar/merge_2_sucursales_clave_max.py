########################## Mezcla de Archivos POR CLAVE MÁXIMA #################
# Genera un unico archivo, en base a otros dos archivos de igual estructura
# y que estan ordenados por alguno de sus datos
# Cuando se encuentran dos "registros" con igual clave de comparacion,
# ambos registros se pasan al nuevo archivo.
# Para esta solucion se utiliza el metodo de clave maxima, por el cual se define una valor,
# que nunca debe ser alcanzado por las claves que se encuentran en el archivo.
def leer_Archivo(archivo):
    linea = archivo.readline()
    return linea.rstrip('\n').split(',') if linea else (MAXIMO,"") #Devuelve 2 vacios

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
    while (codProdS1 != MAXIMO or codProdS2 != MAXIMO):
        if (codProdS1 == codProdS2):
            grabar_Nuevo(arSucGral,codProdS1,cantS1)
            grabar_Nuevo(arSucGral,codProdS2,cantS2)
            codProdS1,cantS1 = leer_Archivo(arSuc1)
            codProdS2,cantS2 = leer_Archivo(arSuc2)
        elif (codProdS1 < codProdS2):
            grabar_Nuevo(arSucGral,codProdS1,cantS1)
            codProdS1,cantS1 = leer_Archivo(arSuc1)
        else:
            grabar_Nuevo(arSucGral,codProdS2,cantS2)
            codProdS2,cantS2 = leer_Archivo(arSuc2)

#########################################################################

MAXIMO = "ZZZ999" #Valor elegido que no puede ser utilizado por ningun codProd en los archivos

arSuc1 = open("sucursal1.csv","r")
arSuc2 = open("sucursal2.csv","r")
arSucGral = open("sucVentas.csv","w")
mezclarArchivos(arSuc1, arSuc2, arSucGral)
arSuc1.close()
arSuc2.close()
arSucGral.close()