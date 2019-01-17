# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 23:40:14 2019

@author: moskovkina

1. В диапазоне натуральных чисел от 2 до 99 определить, 
сколько из них кратны любому из чисел в диапазоне от 2 до 9.
"""
nums = [int(i) for i in range(2, 100)]
num = int(input("Введите число от 2 до 9: "))
cnt = 0

for i in nums:
    if i % num == 0:
        cnt += 1
        
print(f'Количество кратных {num} чисел равно: {cnt}')