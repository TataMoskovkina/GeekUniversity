# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 21:37:15 2019

@author: moskovkina


1. Пользователь вводит данные о количестве предприятий, их наименования и 
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
 Программа должна определить среднюю прибыль (за год для всех предприятий) и 
 вывести наименования предприятий, чья прибыль выше среднего и отдельно 
 вывести наименования предприятий, чья прибыль ниже среднего.
"""

n = int(input("Введите количество предприятий: "))
enterprise = {}
s = 0
for i in range(n):
    ent_name = input(str(i+1) + "-е предприятие: ")
    rev = sum([int(j) for j in input("Введите поквартальную выручку через пробел: ").split()])
    enterprise[ent_name] = rev
    s += rev

rev_avrg = s / n
print(f'\nСредняя выручка за год: {rev_avrg}')
print('-' * 20)
print("Предприятия с выручкой ниже средней:\n")  

for ent_name in enterprise:
    if enterprise[ent_name] > rev_avrg:
        print(ent_name + "\n")
        
print('-' * 20)  
print("Предприятия с выручкой ниже средней:\n")
for ent_name in enterprise:
    if enterprise[ent_name] < rev_avrg:
        print(ent_name + "\n")




  
    