from tkinter import *
ARCHIVE_END = ['','']
debug_mode = False
def obtain_tournament_archive(route, MODE = 'r'):
    """
    recibe una ruta de un archivo y el modo de apertura, devuelve none si no existe
    """
    try:
        tournament_archive = open(route, MODE)
    except:
        tournament_archive = None
    if debug_mode:
        print(tournament_archive)
    return tournament_archive

def obtain_lines(archive):
    """
    Recibe al archivo de obtain_users_archive y retorna las lineas que lo componen
    """
    lines = archive.readlines()
    if lines == '':
        result = ARCHIVE_END
    else:
        result = [tuple(line.strip().split(';')) for line in lines]
        if debug_mode:
            print("el csv: ", result)
    return result

def calculate(tournament,TEAM_DATA = 0, TEAM_NAME = 0, TEAM_WONS = 2, TEAM_DRAWS = 3, TEAM_LOSES = 4):
    """
    recibe el archivo csv y retorna el puntaje de cada equipo en una lista
    """
    team_points_list = []
    teams = obtain_lines(tournament)
    for team in teams:
        team_name = team[TEAM_NAME]
        team_points = int(team[TEAM_WONS]) * 3 + int(team[TEAM_DRAWS]) * 1
        team_points_list.append([team_name,team_points])
    return team_points_list

print(calculate(tournament=obtain_tournament_archive('campeonato.csv')))

