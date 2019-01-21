# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 01:24:10 2019

@author: moskovkina

9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""

from random import randint

M = 5
N = 4
min_lst = []
M_N = [[randint(0,20) for i in range(M)] for i in range(N)]
m_n = [[0 for j in range(N)] for i in range(M)]

#for i in M_N: проверка матрицы
#    print(i)
    
for i in range(N):
    for j in range(M):
        m_n[j][i] = M_N[i][j]

#for i in m_n:   проверка матрицы
#    print(i)
        
for i in m_n:
    min_lst.append(min(i))
    
print('максимальный элемент среди минимальных элементов столбцов матрицы -'
      f'{max(min_lst)}')