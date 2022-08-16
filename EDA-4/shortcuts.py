import statistics as stat
from scipy.stats import ttest_ind
import pandas as pd
import numpy as np
import seaborn as sns

# Это мини-библиотека для сокращения
# объёма ноутбука.

# №1
# Функция для проверки,соответствуют
# ли списки друг другу по длине.

def chk_len(d_1, d_2):
    if len(d_1) != len(d_2):
        print('Длины списков не одинаковой длины:', len(l_1),'и', len(d_2),'. Используйте adj_len(список один, список два, метод).')
    else: print('Длины списков одинаковой длины.')

# №2
# Функция для унификации длин списков.
# На вход принимает два списка и метод.
# Методы: заполнить разницу mean или NaN,
# дописав их как 'mean' или 'nan'.
# Возвращает первый список из пары.

def adj_len(d_1, d_2, method='mean'):
    
    # Делаем копии списков, чтобы они
    # не изменились.
    data = d_1.copy()
    d_1, d_2 = d_1.copy(), d_2.copy()
    dif = len(d_1) - len(d_2)

    # Если разницы нет, просто сортировка.
    if dif == 0:
        return data.sort()
    
    # Подфункция, реализует выбор метода
    def apply_method(data, method):
        if method == 'mean':
            return stat.mean(data)
        elif method == 'nan':
            return np.nan
    
    # Если второй лист больше первого,
    # заполняет разницу NaN или средним,
    # в зависимости от выбора.
    if dif > 0:
        return sorted(data)
    elif dif < 0:
        while dif < 0:
            # then d_1 > d_2
            data.append(apply_method(data, method))
            dif+=1
        return sorted(data)