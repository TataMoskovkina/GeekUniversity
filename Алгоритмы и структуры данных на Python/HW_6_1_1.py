# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 01:34:22 2019

@author: moskovkina

3. Сформировать из введенного числа обратное по порядку входящих в него цифр 
и вывести на экран. Например, если введено число 3486, 
то надо вывести число 6843.
"""
from memory_profiler import profile

@profile
def flip_num(num, flip=0):
    if num == 0:
        return flip
    else:
        flip = (flip * 10) + (num % 10)
        num = num // 10
        return flip_num(num, flip)
    
num = int(input("Введите число, которое требуется перевернуть: "))
print("Перевернутое число: ", flip_num(num))

"""
Line #    Mem usage    Increment   Line Contents
================================================
    13     60.3 MiB     60.2 MiB   @profile
    14                             def flip_num(num, flip=0):
    15     60.3 MiB      0.0 MiB       if num == 0:
    16     60.3 MiB      0.0 MiB           return flip
    17                                 else:
    18     60.3 MiB      0.0 MiB           flip = (flip * 10) + (num % 10)
    19     60.3 MiB      0.0 MiB           num = num // 10
    20     60.3 MiB      0.0 MiB           return flip_num(num, flip)
    
Python 3.6 (интерпритатор Spyder), Windows 10 x64
"""