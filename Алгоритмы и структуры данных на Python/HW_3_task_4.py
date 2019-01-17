# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 00:52:17 2019

@author: moskovkina

4. Определить, какое число в массиве встречается чаще всего.
"""
from random import randint

n = int(input("Введите длинну массива: "))
nums = [randint(0, 10) for i in range(n)]
max_cnt = 0
max_num = 0
for i in nums:
    if nums.count(i) > max_cnt:
        max_num = i
        max_cnt = nums.count(i)

print()
print(f'Число {max_num} встречается в массиве чаще всего: {max_cnt} раз(а)')