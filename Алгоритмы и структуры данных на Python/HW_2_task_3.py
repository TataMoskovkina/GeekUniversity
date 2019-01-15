# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 01:34:22 2019

@author: moskovkina

3. Сформировать из введенного числа обратное по порядку входящих в него цифр 
и вывести на экран. Например, если введено число 3486, 
то надо вывести число 6843.
"""
def flip_num(num, flip=0):
    if num == 0:
        return flip
    else:
        flip = (flip * 10) + (num % 10)
        num = num // 10
        return flip_num(num, flip)
    
num = int(input("Введите число, которое требуется перевернуть: "))
print("Перевернутое число: ", flip_num(num))