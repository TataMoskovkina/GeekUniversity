# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 23:43:15 2018

@author: moskovkina
"""

#Вводятся три разных числа. 
#Найти, какое из них является средним (больше одного, но меньше другого).

print("Введите три целых числа")

a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

if ((a > b) & (a < c)) | ((a < b) & (a > c)):
    print(f"Среднее из трех чисел: {a}")
elif ((b > a) & (b < c)) | ((b < a) & (b > c)):
    print(f"Среднее из трех чисел: {b}")
else:
    print(f"Среднее из трех чисел: {c}") 