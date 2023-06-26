#primero abro los archivos
andres_csv = open('andres.csv','r+')
ezequiel_csv = open('ezequiel.csv','r+')
gustavo_csv = open('gustavo.csv', 'r+')
bianchi_csv = open('bianchi.csv', 'r+')
#crear una funcion que abra el archivo de salida y si no existe lo cree
def open_correctores():
    """abre el archivo correctores"""
    try:
        correctores = open('correctores.csv', 'r+')
    except:
        correctores = open('correctores.csv', 'w')
        correctores.close()
        correctores = open('correctores.csv', 'r+')
    return correctores

correctores = open_correctores()

#definimos los maximos que alcanzaria el archivo al recorrerlo como constantes
MAX_PADRON = '999999'
END_ARCHIVE = MAX_PADRON+',,,,'

#definimos nuestra funcion leer genericamente 
def read_Lines(archive):
    """recibe un archivo, retorar una linea como lista"""
    line = archive.readline()
    return line.rstrip('\n').split(',') if line else END_ARCHIVE.split(',') 
#rstrip se usa para separar una linea de la otra, 
#el parametro que le paso es como quiero que los separe, en estes caso quiero un salto de linea,
#rsplit es el como se sepra la linea internamete al pasarlo a lista, 
#en este caso cada item de la lista se separara en base a las comas
#---------------------------------------------------------------------
#ahora definimos una funcion que grabe el archivo en base a nuestros parametros
def write_archive(archive, padron, note_1, note_2, note_3, note_4):
    """
    recibe un archivo y los componentes de cada linea pra grabarlos en el archivo
    """
    archive.write(padron + ',' + note_1 + ',' + note_2 + ',' + note_3 + ',' + note_4 + '\n')

#ahora hacemos la funcion del merge perse

def merge_archive(correctores, andres_csv, ezequiel_csv, gustavo_csv, bianchi_csv):
    """ 
    recibe los archivos y los mezcla 
    """
    #leer como variables cada item de cada linea de cada archivo
    padron_andres, nota_1_andres, nota_2_andres, nota_3_andres, nota_4_andres = read_Lines(andres_csv)
    padron_ezequiel, nota_1_ezequiel, nota_2_ezequiel, nota_3_ezequiel, nota_4_ezequiel = read_Lines(ezequiel_csv)
    padron_gustavo, nota_1_gustavo, nota_2_gustavo, nota_3_gustavo, nota_4_gustavo = read_Lines(gustavo_csv)
    padron_bianchi, nota_1_bianchi, nota_2_bianchi, nota_3_bianchi, nota_4_bianchi = read_Lines(bianchi_csv)
    # creamos un bucle while que recorrera todos los archivo hasta el final de los mismos en base a una variable que estableceremos 
    # como clave tal que mientras esta 'clave' sea menor al max se seguira recorriendo
    padrones = []
    while int(padron_andres) < int(MAX_PADRON) or int(padron_ezequiel) < int(MAX_PADRON) or int(padron_gustavo) < int(MAX_PADRON) or int(padron_bianchi) < int(MAX_PADRON):
        #definimos una variable que mediante la funcion min() ira devolviendo el valor minimo que recibio en cada iteracion del bucle
        min_padron = min(int(padron_andres), int(padron_ezequiel), int(padron_gustavo), int(padron_bianchi))
        #si la clave es igual al minimo y menor que el fin del archivo se grabara en el archivo
        #para este caso particular agregue una lista y la ordene al final a que necesito el padron ordenado por lista de menor a mayor
        if int(padron_andres) == int(min_padron) and int(padron_andres) < int(MAX_PADRON):
            padrones.append((int(padron_andres), nota_1_andres, nota_2_andres, nota_3_andres, nota_4_andres))
            padron_andres, nota_1_andres, nota_2_andres, nota_3_andres, nota_4_andres = read_Lines(andres_csv)

        if int(padron_ezequiel) == int(min_padron) and int(padron_ezequiel) < int(MAX_PADRON):
            padrones.append((int(padron_ezequiel), nota_1_ezequiel, nota_2_ezequiel, nota_3_ezequiel, nota_4_ezequiel))
            padron_ezequiel, nota_1_ezequiel, nota_2_ezequiel, nota_3_ezequiel, nota_4_ezequiel = read_Lines(ezequiel_csv)

        if int(padron_gustavo) == int(min_padron) and int(padron_gustavo) < int(MAX_PADRON):
            padrones.append((int(padron_gustavo), nota_1_gustavo, nota_2_gustavo, nota_3_gustavo, nota_4_gustavo))
            padron_gustavo, nota_1_gustavo, nota_2_gustavo, nota_3_gustavo, nota_4_gustavo = read_Lines(gustavo_csv)

        if int(padron_bianchi) == int(min_padron) and int(padron_bianchi) < int(MAX_PADRON):
           padrones.append((int(padron_bianchi), nota_1_bianchi, nota_2_bianchi, nota_3_bianchi, nota_4_bianchi))
           padron_bianchi, nota_1_bianchi, nota_2_bianchi, nota_3_bianchi, nota_4_bianchi = read_Lines(bianchi_csv)
        
    padrones.sort(key=lambda x:x[0])
    for padron, nota_1, nota_2, nota_3, nota_4 in padrones:
        write_archive(correctores, str(padron), nota_1, nota_2, nota_3, nota_4)


#ahora invocamos la funcion
merge_archive(correctores,andres_csv, ezequiel_csv, gustavo_csv, bianchi_csv)
#por ultimo cerramos todo
andres_csv.close()
ezequiel_csv.close()
gustavo_csv.close()
bianchi_csv.close()
correctores.seek(0)

#ahora vamos con el apareo usamos practicamente la msima estructura
def open_parcial1():
    try:
        parcial1 = open('parcial_1.csv', 'r+')
    except:
        parcial1 = open('parcial_1.csv', 'w')
        parcial1.close()
        parcial1 = open('parcial_1.csv', 'r+')
    return parcial1

parcial1 = open_parcial1()


def write_mating_archive(archive, padron, nota):
    """
    recibe uin archivo, sus elementos y los escribe
    """
    archive.write(padron + ',' + nota + '\n')


def mating_archive(parcial1):
    """
    recibe el archivo y devuelve las notas
    """
    padron, nota_1, nota_2, nota_3, nota_4 = read_Lines(correctores)
    
    while int(padron) < int(MAX_PADRON):
        suma_nota_final = float(nota_1) + float(nota_2)+ float(nota_3) + float(nota_4)
        nota_final = suma_nota_final/4
        write_mating_archive(parcial1, str(padron), str(nota_final))
        padron, nota_1, nota_2, nota_3, nota_4 = read_Lines(correctores)
#merge mezcla, apareo actualiza en base al merge



mating_archive(parcial1)        
correctores.close()
parcial1.close()

#------------------------------------------------------------------------------------------
#ejercicio 3: todo lo que sigue es para perfeccionar lo anterior
END_ARCHIVE_PARCIAl = MAX_PADRON+','
END_ARCHIVE_CURSO = MAX_PADRON+',,,'


def read_lines_parcial(archive):
    line = archive.readline()
    return line.rstrip('\n').split(',') if line else END_ARCHIVE_PARCIAl.split(',') 

def read_lines_curso(archive):
    line = archive.readline()
    return line.rstrip('\n').split(',') if line else END_ARCHIVE_CURSO.split(',') 

def write_curso_parcial(archive, padron, nombre, apellido, nota):
    archive.write(padron + ',' + nombre + ',' + apellido + ','+ nota + '\n')

def open_parcial1_curso():
    try:
        parcial1_curso = open('7540_1C2020_parcial1.csv', 'r+')
    except:
        parcial1_curso = open('7540_1C2020_parcial1.csv', 'w')
        parcial1_curso.close()
        parcial1_curso = open('7540_1C2020_parcial1.csv', 'r+')
    return parcial1_curso

curso = open('7540_1C2020.csv', 'r+')
parcial1 = open('parcial_1.csv', 'r+')
parcial1_curso = open_parcial1_curso()


def mateing_parcial1_curso(parcial1_curso, curso, parcial1):

    padron_parcial, nota = read_lines_parcial(parcial1)
    padron_curso, nombre, apellido, correo = read_lines_curso(curso)

    while int(padron_parcial) < int(MAX_PADRON) or int(padron_curso) < int(MAX_PADRON):
        while padron_parcial == padron_curso < MAX_PADRON:
            padron = padron_parcial
            write_curso_parcial(parcial1_curso, padron, nombre, apellido, nota)
            padron_parcial, nota = read_lines_parcial(parcial1)
            padron_curso, nombre, apellido, correo = read_lines_curso(curso)

mateing_parcial1_curso(parcial1_curso, curso, parcial1)
curso.seek(0)
parcial1.close()


def write_curso_parcial_aprobado(archive ,correo, nombre, nota):
    archive.write('Para: ' + correo + 'Asunto: Aprobaste el parcial de Algoritmos I! :)' + ' Contenido: hola' + nombre + '! Aprobaste el parcial de Algoritmos I con un ' + nota + '\n')

def write_curso_parcial_desaprobado(archive ,correo, nombre, nota):
    archive.write('Para: ' + correo + 'Asunto: Reprobaste el parcial de Algoritmos I! :(' + ' Contenido: hola' + nombre + '! Reprobaste el parcial de Algoritmos I con un ' + nota + ' .El recuperatorio es el jueves 2/7. Saludos!' + '\n')

def open_aprobados():
    try:
        aprobados = open('aprobados.txt', 'r+')
    except:
        aprobados = open('aprobados.txt', 'w')
        aprobados.close()
        aprobados = open('aprobados.txt', 'r+') 
    return aprobados

def open_reprobados():
    try:
        reprobados = open('reprobados.txt', 'r+')
    except:
        reprobados = open('reprobados.txt', 'w')
        reprobados.close()
        reprobados = open('reprobados.txt', 'r+') 
    return reprobados

aprobados = open_aprobados()
reprobados = open_reprobados()

def apareo_curso_parcial_aprobados(aprobados, reprobados, parcial1_curso, curso):
    padron_parcial, nombre, apellido, nota = read_lines_curso(parcial1_curso)
    padron_curso, nombre, apellido, correo = read_lines_curso(curso)

    while int(padron_parcial) < int(MAX_PADRON) or int(padron_curso) < int(MAX_PADRON):
        while padron_parcial == padron_curso < MAX_PADRON and float(nota) >= 4.0:
            write_curso_parcial_aprobado(aprobados, correo, nombre, nota)
            padron_parcial, nombre, apellido, nota = read_lines_curso(parcial1_curso)
            padron_curso, nombre, apellido, correo = read_lines_curso(curso)
        while padron_parcial == padron_curso < MAX_PADRON and float(nota) < 4.0:
            write_curso_parcial_desaprobado(reprobados, correo, nombre, nota)
            padron_parcial, nombre, apellido, nota = read_lines_curso(parcial1_curso)
            padron_curso, nombre, apellido, correo = read_lines_curso(curso)

apareo_curso_parcial_aprobados(aprobados, reprobados, parcial1_curso, curso)

aprobados.close()
reprobados.close()
curso.close()
parcial1_curso.close()

