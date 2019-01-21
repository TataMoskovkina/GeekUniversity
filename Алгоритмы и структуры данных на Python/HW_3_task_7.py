# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 01:22:55 2019

@author: moskovkina

7. В одномерном массиве целых чисел определить два наименьших элемента. 
Они могут быть как равны между собой (оба являться минимальными), 
так и различаться.
"""
from random import randint

n = int(input("Введите длинну массива: "))
nums = [randint(0, 20) for i in range(n)]
print(nums) #проверка

min_1 = min(nums)
nums.pop(nums.index(min(nums)))
print(nums) #проверка

min_2 = min(nums)

print(f'Первые два наименьших числа в массиве равны: {min_1} и {min_2}')