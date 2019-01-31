# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 01:05:39 2019

@author: moskovkina

5. В массиве найти максимальный отрицательный элемент. 
Вывести на экран его значение и позицию в массиве.
"""
from random import randint
from pympler import asizeof

n = int(15)
nums = [randint(-20, 10) for i in range(n)]
max_neg_num = 0

for i in nums:
    if i < 0:
        if i < max_neg_num:
            max_neg_num = i

print()
print(f'Максимальный отрицательный элемент: {max_neg_num}, '
      f'его индекс [{nums.index(max_neg_num)}]')

def show_sizeof(obj):
    print("Объект: {0}, Тип: {1}, Размер: {2} байт".format(obj, 
          obj.__class__, asizeof.asizeof(obj)))

show_sizeof(n)
show_sizeof(nums)

"""
Объект: 15, Тип: <class 'int'>, Размер: 32 байт
Объект: [-10, 0, -15, -3, -8, -17, 4, 5, -15, -7, 7, -19, -19, -15, 2], 
Тип: <class 'list'>, Размер: 664 байт

Python 3.6 (интерпритатор Spyder), Windows 10 x64
"""