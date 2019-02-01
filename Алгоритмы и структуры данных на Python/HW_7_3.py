# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 00:43:00 2019

@author: moskovkina

3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. 
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его 
на две равные части: в одной находятся элементы, которые не меньше медианы, 
в другой – не больше медианы. Задачу можно решить без сортировки исходного массива. 
Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках
"""

import random

def gnome_sort(orig_list):
    i = 1
    while i < len(orig_list):
        if (orig_list[i - 1] <= orig_list[i]):
            i += 1
        else:
            tmp = orig_list[i]
            orig_list[i] = orig_list[i - 1]
            orig_list[i - 1] = tmp
            i-= 1
            if (i == 0):
                i = 1
    return orig_list

orig_list = [random.randint(0, 100) for i in range(2*(int(random.random()*100 // 10) + 1))]        
print(orig_list)

sort_list = gnome_sort(orig_list)
mediana = sort_list[len(sort_list) // 2]

print(sort_list)
print(mediana)

"""
Без сортировки не получилось, будет интересно посмотреть на реализацию когда будете ДЗ разбирать.
Использовала Гномью(глупую) сортировку.
"""
 