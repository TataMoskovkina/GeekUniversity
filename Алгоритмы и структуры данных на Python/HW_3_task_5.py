# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 01:05:39 2019

@author: moskovkina

5. В массиве найти максимальный отрицательный элемент. 
Вывести на экран его значение и позицию в массиве.
"""
from random import randint

n = int(input("Введите длинну массива: "))
nums = [randint(-20, 10) for i in range(n)]
max_neg_num = 0

for i in nums:
    if i < 0:
        if i < max_neg_num:
            max_neg_num = i

print()
print(f'Максимальный отрицательный элемент: {max_neg_num}, '
      f'его индекс [{nums.index(max_neg_num)}]')