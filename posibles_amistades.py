def posibles_amistades(personas, intereses_afines):
    personas_amigas = []
    for intereses in range (1,len(personas),2):
        nombre_persona = personas[intereses - 1]
        coinciden = 0
        interes = 0
        while coinciden < 2 and interes < len(personas[intereses]):
            if personas[intereses][interes] in intereses_afines:
                coinciden += 1
            if coinciden == 2:
                personas_amigas.append(nombre_persona)
            interes += 1
    return personas_amigas
personas = ["Camila",["natacion","gimnasio","voley","futbol"],"Mario",["natacion","basquet","gimnasio","cine"],"Rosa",["cine","teatro","natacion"]]
intereses_afines = ["natacion","teatro","cine","tenis"]
intereses_afines2 = ["cine","tenis","ajedrez"]
print(posibles_amistades(personas,intereses_afines))
print(posibles_amistades(personas,intereses_afines2))