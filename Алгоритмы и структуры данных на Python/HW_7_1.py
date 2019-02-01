# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 23:39:26 2019

@author: moskovkina

1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, 
заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный 
и отсортированный массивы. Сортировка должна быть реализована в виде функции. 
По возможности доработайте алгоритм (сделайте его умнее).
"""
import random
import timeit
from memory_profiler import profile

@profile
def bubble_sort(orig_list):
    n = 1
    k = 0
    while n < len(orig_list):
        for i in range(len(orig_list)-n):
            if orig_list[i] < orig_list[i+1]:
                orig_list[i], orig_list[i+1] = orig_list[i+1], orig_list[i]
                k = 1
        if k == 0:
            break            
        n +=1
    return orig_list
        

orig_list = [random.randint(-100, 100) for i in range(10)]

print(orig_list)
print(bubble_sort(orig_list))
print(timeit.timeit("bubble_sort(orig_list)", setup="from __main__ import bubble_sort, orig_list", number=100))

"""
Результат сортировки:
[59, 38, -42, -20, -24, 9, -54, 29, 37, 78]
[78, 59, 38, 37, 29, 9, -20, -24, -42, -54]

Закоментированные строки это улучшение алгоритма. Если за проход по всему массиву 
не было совершено ни одной сортировки, то работа функции прекращается.

Если измерить время работы без улучшения и с улучшением, то можно увидеть следующие результаты:
    Без улучшения: 0.0009809281514776558
    С улучшением: 0.000157895879510761
    
Разница не так велика, но если мы увеличим массив до 1000 элементов, то увидим следующий результат:
    Без улучшения: 5.36070089980899
    С улучшением: 0.011878901755153493
Вот тут уже разница поражает. Улучшение явно пошло алгоритму на пользу. 

Замер же используемой памяти дает одинаковые результаты:
    
    Без улучшения: 
        
Line #    Mem usage    Increment   Line Contents
================================================
    16     50.3 MiB     50.3 MiB   @profile
    17                             def bubble_sort(orig_list):
    18     50.3 MiB      0.0 MiB       n = 1
    19                             #    k = 0
    20     50.3 MiB      0.0 MiB       while n < len(orig_list):
    21     50.3 MiB      0.0 MiB           for i in range(len(orig_list)-n):
    22     50.3 MiB      0.0 MiB               if orig_list[i] < orig_list[i+1]:
    23                                             orig_list[i], orig_list[i+1] = orig_list[i+1], orig_list[i]
    24                             #                k = 1
    25                             #        if k == 0:
    26                             #            break            
    27     50.3 MiB      0.0 MiB           n +=1
    28     50.3 MiB      0.0 MiB       return orig_list
    
    С улучшением:

Line #    Mem usage    Increment   Line Contents
================================================
    16     50.5 MiB     50.5 MiB   @profile
    17                             def bubble_sort(orig_list):
    18     50.5 MiB      0.0 MiB       n = 1
    19     50.5 MiB      0.0 MiB       k = 0
    20     50.5 MiB      0.0 MiB       while n < len(orig_list):
    21     50.5 MiB      0.0 MiB           for i in range(len(orig_list)-n):
    22     50.5 MiB      0.0 MiB               if orig_list[i] < orig_list[i+1]:
    23                                             orig_list[i], orig_list[i+1] = orig_list[i+1], orig_list[i]
    24                                             k = 1
    25     50.5 MiB      0.0 MiB           if k == 0:
    26     50.5 MiB      0.0 MiB               break            
    27                                     n +=1
    28     50.5 MiB      0.0 MiB       return orig_list
"""

