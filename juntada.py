import doctest
def juntada(diccionario):
    """
    >>> dicc_1 = {'Tomas': ['LUN','MIER','SAB'],'Emi': ['LUN','MIER','VIER','SAB','DOM'], 'Lucas':['LUN','SAB','DOM'],'Ceni':['LUN','VIE','SAB']}
    >>> juntada(dicc_1)
    ['LUN', 'SAB']
    """
    dias_disponibles = []
    dias_disponibles_para_todos = []
    for dias in diccionario.values():
        dias_disponibles += dias
    for dias_convenientes in dias_disponibles:
        if dias_disponibles.count(dias_convenientes) == len(diccionario) and dias_convenientes not in dias_disponibles_para_todos:
            dias_disponibles_para_todos.append(dias_convenientes)
    return dias_disponibles_para_todos
doctest.testmod()