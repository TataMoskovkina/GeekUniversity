# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 01:11:29 2019

@author: moskovkina

6. В одномерном массиве найти сумму элементов, находящихся между минимальным 
и максимальным элементами. 
Сами минимальный и максимальный элементы в сумму не включать.
"""
from random import randint

n = int(input("Введите длинну массива: "))
nums = [randint(0, 20) for i in range(n)]
summ = 0

if nums.index(min(nums)) > nums.index(max(nums)):
    for i in range(nums.index(max(nums)) + 1, nums.index(min(nums))):
        summ += nums[i]
else:
    for i in range(nums.index(min(nums)) + 1, nums.index(max(nums))):
        summ += nums[i]

print()
print(f'Cумма элементов, находящихся между минимальным {min(nums)} '
            f'и максимальным элементами {max(nums)} равна {summ}.')