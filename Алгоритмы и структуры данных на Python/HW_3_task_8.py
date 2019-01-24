# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 01:23:31 2019

@author: moskovkina

8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. 
Программа должна вычислять сумму введенных элементов каждой строки и записывать
 ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.
"""

M = 5
N = 4
a = []
for i in range(N):
    b = []
    s = 0
    print(f'{i+1}-я строка')
    for j in range(M-1):
        n = int(input())
        s += n
        b.append(n)
    b.append(s)
    a.append(b)
 
for i in a:
    print(i)