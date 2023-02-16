import statistics as stat
from scipy.stats import ttest_ind
import pandas as pd
import numpy as np
import seaborn as sns
import IPython.display


# Это мини-библиотека для сокращения
# объёма ноутбука.

# №1
#
# Функция для проверки,соответствуют
# ли списки друг другу по длине.

def chk_len(d_1, d_2):
    if len(d_1) != len(d_2):
        print('Длины списков не одинаковой длины:', len(d_1),'и', len(d_2),'. Используйте adj_len(список_один, список_два, метод).')
    else: print('Длины списков одинаковой длины.')

# №2
#
# Функция для унификации длин списков.
# На вход принимает два списка и метод.
# Методы: заполнить разницу средним,
# медианным или NaN значением,
# дописав их как 'mean', 'med' или 'nan'.
#
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
    
    # Подфункция, реализует выбор метода.
    def apply_method(data, method):
        if method == 'mean':
            return stat.mean(data)
        elif method == 'med':
            return stat.median(data)
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
    
# №3
#
# Эту команду я нашёл на StackOverflow:
# https://stackoverflow.com/a/50899244
# Она служит для расположения двух DataFrame
# на одном уровне.
def tables_in_rows(df1, df2, df3):
    
    df1_styler = df1.style.set_table_attributes("style='display:inline'").set_caption('Добавить среднее')
    df2_styler = df2.style.set_table_attributes("style='display:inline'").set_caption('Добавить медиану')
    df3_styler = df3.style.set_table_attributes("style='display:inline'").set_caption('Добавить NaN')
    
    IPython.display.display_html(df1_styler._repr_html_()+df2_styler._repr_html_()+df3_styler._repr_html_(), raw=True)

# №3
#
# Эта команда прогоняет T-тeст на двух
# рядах датафрейма.
def t_test(data, alpha):
    H0 = 'Нет значимой разницы между средним размером раковины мидий в двух городах.'
    Ha = 'Есть значимая разница между средним размером раковины мидий в двух городах.'
    
    print('\n' + "*** Результаты независимого T-теста ***")
    test_results = ttest_ind(data.iloc[:,0], data.iloc[:,1], equal_var=True, nan_policy='omit')

    p = round(test_results[1],2)

    if p>alpha:
        print(f"{p} > {alpha}. Мы не можем отвергнуть нулевую гипотезу. {H0}")
    else:
        print(f"{p} <= {alpha}. Мы отвергаем нулевую гипотезу. {Ha}")
