# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 00:18:37 2019

@author: moskovkina

2. Написать программу сложения и умножения двух шестнадцатеричных чисел. 
При этом каждое число представляется как массив, элементы которого это цифры числа. 
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и 
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], 
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

class Hex_dec:
    def __init__(self, x):
        self.x = int(''.join(x).lower(), 16)
        

    def __add__(self, obj):
        self.summa = str(hex(self.x + obj.x)).upper()
        
    def __mul__(self, obj):
        self.mult = str(hex(self.x * obj.x)).upper()
        
x = list(tuple(input("Введите первое число: ")))
y = list(tuple(input("Введите второе число: ")))
a = Hex_dec(x)
b = Hex_dec(y)
a + b
a * b

summa = list(tuple(a.summa[2::]))
mult = list(tuple(a.mult[2::]))

print(f'\nСумма: {summa}')
print(f'\nПроизведение: {mult}')