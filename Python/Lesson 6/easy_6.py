# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 23:19:51 2018

@author: mosko
"""

# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math

'''class Triangle:
    def __init__(self,A, B, C):
        
        def len_storon(p1, p2):
            return math.sqrt((p2[0]-p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)
        
        self.A = A
        self.B = B
        self.C = C
        
        self.AB = len_storon(self.A, self.B)
        self.BC = len_storon(self.B, self.C)
        self.CA = len_storon(self.C, self.A)
        
    def per(self):
        return self.AB + self.BC + self.CA
    
    def polu_per(self):
        return self.per() / 2
    
    def S_triang(self):
        return math.sqrt((self.polu_per() - self.AB)*(self.polu_per() -
                          self.BC)*(self.polu_per() - self.CA)*self.polu_per())
    
    def height_tiang(self):
        return self.S_triang() / (self.AB / 2)
    
ABC = Triangle((2,1), (2,4), (3,1))

print(ABC.per())
print(ABC.S_triang())
print(ABC.height_tiang())'''       

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapezium():
    def __init__(self,A, B, C, D):
        def len_storon(p1, p2):
            return math.sqrt((p2[0]-p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)
        
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        
        def S_triang(x, y, z):
            polu_per = (x + y + z) / 2
            
            return math.sqrt((polu_per - x) * (polu_per - y) *
                             (polu_per - z) * polu_per)
            
        self.AB = len_storon(self.A, self.B)
        self.BC = len_storon(self.B, self.C)
        self.CD = len_storon(self.C, self.D)
        self.DA = len_storon(self.D, self.A)
        self.diag_AC = len_storon(self.A, self.C)
        self.diag_BD = len_storon(self.B, self.D)
        self.S_trap = S_triang(self.AB, self.diag_BD, self.DA) + S_triang(self.BC, self.CD, self.diag_BD)
                 
    def per(self):
        return self.AB + self.BC + self.CD + self.DA
    
    def IsTrapEqu(self):
        if self.diag_AC == self.diag_BD:
            return True
        else:
            return False
            
trap = Trapezium((2,1),(3,4),(6,4),(7,1))

print(trap.AB, trap.BC, trap.CD, trap.DA)
print(trap.per())
print(trap.S_trap)
print(trap.IsTrapEqu())

      
    
        
        