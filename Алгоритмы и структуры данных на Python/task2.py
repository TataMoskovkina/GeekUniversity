# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 23:40:08 2018

@author: mosko
"""

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

m = a

if m < b:
    m = b
if m < c:
    m = c
    
print(m)