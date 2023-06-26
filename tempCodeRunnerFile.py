while padron_examenes == padron_candid < MAX_PADRON: 
            if int(nota) == 10:
                write_candidatos(candidatos, padron_candid, codigo, prom_cand)
                padron_examenes, codigo, nota = read_Lines_alumnos(examenes)
                padron_alumnos, cant_materias, prom = read_Lines_alumnos(alumnos)
                padron_candid, cant_materias_cand, prom_cand = read_Lines_alumnos(new_alumnos)