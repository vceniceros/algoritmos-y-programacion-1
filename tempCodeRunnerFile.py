if int(ocupadas) > int(camas):
            write_master(error, cod_master, camas, ocupadas)
        cod_master, camas, ocupadas = read_lines_Master(maestro)
        cod_novedades, dni, estado = read_lines_Master(novedades)