# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 23:33:02 2019

@author: moskovkina

2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, 
заданный случайными числами на промежутке [0; 50). 
Выведите на экран исходный и отсортированный массивы.

"""

import random

def merge(left,right):
    sort_list = []
    while left and right:
        if left[0] < right[0]:
            sort_list.append(left.pop(0))
        else:
            sort_list.append(right.pop(0))
    if left:
        sort_list.extend(left)
    if right:
        sort_list.extend(right)
    return sort_list
  
def merge_sort(orig_list):
    if len(orig_list) >= 2:
        middle = int(len(orig_list) / 2)
        orig_list = merge(merge_sort(orig_list[:middle]), merge_sort(orig_list[middle:]))
    return orig_list
    
orig_list = [round(random.uniform(0, 50), 5) for i in range(50)]
print(orig_list)
print(merge_sort(orig_list))

