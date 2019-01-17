# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 14:29:05 2019

@author: moskovkina

9. Среди натуральных чисел, которые были введены, 
найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""
n = int(input("Введите первое число: "))
max_num = 0
max_sum = 0

def max_number(n):
    global max_num, max_sum
    
    if n == 0:
        return max_num, max_sum
    m = n
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    if s > max_sum:
        max_num = m
        max_sum = s
    
    n = int(input("Введите еще одно число: "))
    return max_number(n)    

max_number(n)

print(f'Максимальное число равно: {max_num}, сумма его чисел равна: {max_sum}')