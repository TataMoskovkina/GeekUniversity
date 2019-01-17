# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 00:19:20 2019

@author: moskovkina

3. В массиве случайных целых чисел поменять местами минимальный и 
максимальный элементы.
"""
from random import randint

n = int(input("Введите длинну массива: "))
nums = [randint(-5, 5) for i in range(n)]
    
print()
print(f'Первый массив {nums}')    

nums[nums.index(min(nums))], nums[nums.index(max(nums))] = max(nums), min(nums)

print()
print(f'Второй массив {nums}')

