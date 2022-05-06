from numpy import nan
import pandas as pd

def get_occupation(arg):
    if pd.isna(arg):
        return(np.nan)
    args = str(arg)
    
    fullday = False
    partday = False
    project = False
    student = False
    forfree = False
    
    if 'ч' in args:
        fullday = True
    if 'по' in args:
        partday = True
    if 'пр' in args:
        project = True
    if 'ж' in args:
        student = True
    if 'вол' in args:
        forfree = True

    return pd.Series({'Полная занятость': fullday,
                      'Частичная занятость': partday,
                      'Проектная работа' : project,
                      'Стажировка': student,
                      'Волонтёрство': forfree})

def get_occupation_prefs(arg):
    if pd.isna(arg):
        return(np.nan)
    
    fullday = False
    floatin = False
    changes = False
    goesfar = False
    distant = False
    
    if 'по' in arg:
        fullday = True
    if 'ги' in arg:
        floatin = True
    if 'мен' in arg:
        changes = True
    if 'х' in arg:
        goesfar = True
    if 'да' in arg:
        distant = True

    return pd.Series({'Полный день': fullday,
                      'Гибкий график': floatin,
                      'Сменный график' : changes,
                      'Вахтовый метод': goesfar,
                      'Удалённая работа': distant})