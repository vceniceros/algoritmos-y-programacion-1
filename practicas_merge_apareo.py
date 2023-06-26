MAX_PADRON = '999999'
END_ARCHIVE = MAX_PADRON+',,'

def open_candidatos_ayte():
    try:
        candidatos = open('candidatos_ayte.csv', 'r+')
    except:
        candidatos = open('candidatos_ayte.csv', 'w')
        candidatos.close()
        candidatos = open('candidatos_ayte.csv', 'r+')
    return candidatos
def open_new_alumnos():
    try:
        new_alumnos = open('new_alumnos.csv', 'r+')
    except:
        new_alumnos = open('new_alumnos.csv', 'w')
        new_alumnos.close()
        new_alumnos = open('new_alumnos.csv', 'r+')
    return new_alumnos

examenes = open('Examenes.csv','r+')
alumnos = open('Alumnos.csv', 'r+')
candidatos = open_candidatos_ayte()
new_alumnos = open_new_alumnos()

def read_Lines_alumnos(archive):
    """recibe un archivo, retorar una linea como lista"""
    line = archive.readline()
    return line.rstrip('\n').split(',') if line else END_ARCHIVE.split(',') 

def write_alumnos(archivo, padron, cant_materias, prom):
    archivo.write(padron + ',' + cant_materias + ',' + prom + '\n')

def write_candidatos(archivo, padron, codigo, prom):
    archivo.write(padron + ',' + codigo + ',' + prom + '\n')

def apareo_alumnos(candidatos, alumnos, examenes):

    padron_examenes, codigo, nota = read_Lines_alumnos(examenes)
    padron_alumnos, cant_materias, prom = read_Lines_alumnos(alumnos)
    padron_candid, cant_materias_cand, prom_cand = read_Lines_alumnos(new_alumnos)
    while int(padron_examenes) < int(MAX_PADRON) or int(padron_alumnos) < int(MAX_PADRON):
        while padron_alumnos == padron_examenes < MAX_PADRON:
            
            padron = padron_examenes
            new_cant_materias = int(cant_materias) + 1
            new_prom_parcial = float(prom)*float(cant_materias)+float(nota)
            new_prom = new_prom_parcial/new_cant_materias
            
            write_alumnos(new_alumnos, padron, str(new_cant_materias), str(new_prom))
            if int(nota) == 10:
                write_candidatos(candidatos, padron, codigo, str(new_prom))
            
            padron_examenes, codigo, nota = read_Lines_alumnos(examenes)
            padron_alumnos, cant_materias, prom = read_Lines_alumnos(alumnos)
          
        
apareo_alumnos(candidatos, alumnos, examenes)