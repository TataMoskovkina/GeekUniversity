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
from pympler import asizeof

class Hex_dec:
    def __init__(self, x):
        self.x = int(''.join(x).lower(), 16)
        

    def __add__(self, obj):
        self.summa = str(hex(self.x + obj.x)).upper()
        
    def __mul__(self, obj):
        self.mult = str(hex(self.x * obj.x)).upper()

class Hex_dec_slots:
    __slots__=['x']
    def __init__(self, x):
        self.x = int(''.join(x).lower(), 16)
        

    def __add__(self, obj):
        self.summa = str(hex(self.x + obj.x)).upper()
        
    def __mul__(self, obj):
        self.mult = str(hex(self.x * obj.x)).upper()
        
x = list(tuple('987465'))

a = Hex_dec(x)
a_s = Hex_dec_slots(x)

print("Размер занимаемой памяти без слотов: ", asizeof.asizeof(a))
print("Размер занимаемой памяти со слотами: ", asizeof.asizeof(a_s))

"""
Размер занимаемой памяти без слотов:  256
Размер занимаемой памяти со слотами:  80

Python 3.6 (интерпритатор Spyder), Windows 10 x64
"""