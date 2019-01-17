# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 00:58:23 2019

@author: moskovkina

2. Посчитать четные и нечетные цифры введенного натурального числа. 
Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) 
и 2 нечетные (3 и 5).
"""

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