def open_update_master():
    try:
        new_master = open('Maestro_actualizado.csv', 'r+')
    except:
        new_master = open('Maestro_actualizado.csv', 'w')
        new_master.close()
        new_master = open('Maestro_actualizado.csv', 'r+')
    return new_master
def open_error_log():
    try:
        error = open('Error_log.csv', 'r+')
    except:
        error = open('Error_log.csv', 'w')
        error.close()
        error = open('Error_log.csv', 'r+')
    return error

MAX_PROV = '25'
FIN_ARCHIVO = MAX_PROV+',,'
INGRESADO = 'ingresado'
INTERNADO = 'internado'
ALTA = 'alta'


maestro = open('Maestro.csv','r+')
novedades = open('Novedades.csv','r+')
new_master = open_update_master()
error = open_error_log()

def read_lines_Master(archive):
    line = archive.readline()
    return line.rstrip('\n').split(',') if line else FIN_ARCHIVO.split(',')

def write_master(archive, cod, camas, ocupadas):
    archive.write(cod + ',' + camas + ',' + ocupadas + '\n')

def apareo_master(new_master, novedades, maestro, error):
    cod_master, camas, ocupadas = read_lines_Master(maestro)
    cod_novedades, dni, estado = read_lines_Master(novedades)

    while int(cod_master) < int(MAX_PROV) and int(cod_novedades) < int(MAX_PROV):
        while int(cod_master) == int(cod_novedades) < int(MAX_PROV):
            if estado == INGRESADO and int(camas) > int(ocupadas)+1:
                ocup = int(ocupadas)
                ocup+= 1
                write_master(new_master, cod_master, camas, str(ocup))
            elif estado == INGRESADO and int(camas) < int(ocupadas)+1:
                ocup = int(ocupadas)
                ocup+= 1
                write_master(error, cod_master, camas, str(ocup))
            elif estado == INTERNADO:
                write_master(new_master, cod_master, camas, ocupadas)
            elif estado == ALTA and int(ocupadas) - 1 >= 0:
                ocup = int(ocupadas)
                ocup -= 1
                write_master(new_master, cod_master, camas, str(ocup))
            elif estado == ALTA and int(ocupadas) - 1 < 0:
                ocup = int(ocupadas)
                ocup -= 1
                write_master(error, cod_master, camas, str(ocup))
            cod_novedades, dni, estado = read_lines_Master(novedades)
        
        while int(cod_master) < int(MAX_PROV):
            write_master(new_master, cod_master, camas, ocupadas)
            cod_master, camas, ocupadas = read_lines_Master(maestro)

apareo_master(new_master, novedades, maestro, error)
maestro.close()
new_master.close()
novedades.close()
error.close()