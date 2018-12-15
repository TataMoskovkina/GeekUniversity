# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 23:50:45 2018

@author: mosko
"""

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if a > b:
    if a > c:
        print(f'max = {a}')
    else:
        print(f'max = {c}')
else:
    if b > c:
        print(f'max = {b}')
    else:
        print(f'max = {c}')