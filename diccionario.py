def tabla_de_posiciones(equipos):
    NDE = 0
    PG= 1
    PE = 2 
    PP = 3
    tdp={}
    for equipo in equipos:
        if equipo[NDE] not in tdp:
            tdp[equipo[NDE]] = 3*equipo[PG]+equipo[PE]
        else: 
           tdp[equipo[NDE]] += 3*equipo[PG]+equipo[PE]
    return tdp

equips=[('riBer',20,0,0),('boca',8,2,10),('san lorenzo', 10,10,0),('independiente',0,2,18)]
tabla_ordenada = sorted(tabla_de_posiciones(equips).items(),reverse=True,key = lambda x:x[1])
print(tabla_ordenada)