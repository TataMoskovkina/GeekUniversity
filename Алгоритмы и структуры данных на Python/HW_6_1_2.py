# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 00:58:23 2019

@author: moskovkina

2. Посчитать четные и нечетные цифры введенного натурального числа. 
Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) 
и 2 нечетные (3 и 5).
"""
from memory_profiler import profile

@profile
def cnt_even_odd(num, even=0, odd=0):
    if num == 0:
        return even, odd
    else:
        n = num % 10
        num = num // 10
        if n % 2 == 0:
            even += 1
            return cnt_even_odd(num, even, odd)
        else:
            odd += 1
            return cnt_even_odd(num, even, odd)
        
num = int(input("Введите число: "))
print("Количество четных и нечетных цифр в числе равно: ", cnt_even_odd(num))

"""
Line #    Mem usage    Increment   Line Contents
================================================
    13     60.4 MiB     60.3 MiB   @profile
    14                             def cnt_even_odd(num, even=0, odd=0):
    15     60.4 MiB      0.0 MiB       if num == 0:
    16     60.4 MiB      0.0 MiB           return even, odd
    17                                 else:
    18     60.4 MiB      0.0 MiB           n = num % 10
    19     60.4 MiB      0.0 MiB           num = num // 10
    20     60.4 MiB      0.0 MiB           if n % 2 == 0:
    21     60.4 MiB      0.0 MiB               even += 1
    22     60.4 MiB      0.0 MiB               return cnt_even_odd(num, even, odd)
    23                                     else:
    24     60.4 MiB      0.0 MiB               odd += 1
    25     60.4 MiB      0.0 MiB               return cnt_even_odd(num, even, odd)
    
Python 3.6 (интерпритатор Spyder) Windows 10 x64
"""