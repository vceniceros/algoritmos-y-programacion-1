equips=[('river',20,0,0),('san lorenzo', 10,10,0),('boca',8,2,10),('independiente',0,2,18)]
NDE = 0
PG= 1
PE = 2 
PP = 3
def tabla_de_posiciones(equipos):
    tdp =[]
    for equipo in equipos:
      tdp.append((equipo[NDE],3*equipos[PG]+equipos[PE]))
    return tdp
print(tabla_de_posiciones(equips))