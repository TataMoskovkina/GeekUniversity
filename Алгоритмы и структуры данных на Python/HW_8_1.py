# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 02:25:26 2019

@author: moskovkina

Определение количества различных подстрок с использованием хэш-функции. 
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв. 
Требуется найти количество различных подстрок в этой строке.
"""
S = str(input("Введите строку: "))

substr = set()

for i in range(len(S)):
    for j in range(len(S)-1 if i == 0 else len(S), i, -1):
        substr.add(hash(S[i:j]))
        
print(f'Количество подстрок в данной строке: {len(substr)}')
