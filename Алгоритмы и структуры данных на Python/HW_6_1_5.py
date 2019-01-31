# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 00:41:58 2019

@author: moskovkina
"""
from memory_profiler import profile

#нахождение i - Го простого числа без решета Эратосфена
n = 50


@profile
def simple_num(n,n_sim=[]):
    for i  in range(2, n ** 2):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            n_sim.append(i)
     
    return n_sim[n-1]

print(simple_num(n))


@profile
def eratosfen(n):
    a = [int(i) for i in range(n ** 2)]
    a[1] = 0

    m = 2
    while m < n ** 2:
        if a[m] != 0:
            j = m *2
            while j < n ** 2:
                a[j] = 0
                j = j + m
        m += 1

    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])
        
    return(b[n-1])
    
print(eratosfen(n))
 
     
"""
Результат замера используемой памяти с помощью memory_profiler :
    
Line #    Mem usage    Increment   Line Contents
================================================
    13     73.8 MiB     73.8 MiB   @profile
    14                             def simple_num(n,n_sim=[]):
    15     73.8 MiB      0.0 MiB       for i  in range(2, n ** 2):
    16     73.8 MiB      0.0 MiB           for j in range(2, i):
    17     73.8 MiB      0.0 MiB               if i % j == 0:
    18     73.8 MiB      0.0 MiB                   break
    19                                     else:
    20     73.8 MiB      0.0 MiB               n_sim.append(i)
    21                                  
    22     73.8 MiB      0.0 MiB       return n_sim[n-1]

Line #    Mem usage    Increment   Line Contents
================================================
    27     73.8 MiB     73.8 MiB   @profile
    28                             def eratosfen(n):
    29     73.8 MiB      0.0 MiB       a = [int(i) for i in range(n ** 2)]
    30     73.8 MiB      0.0 MiB       a[1] = 0
    31                             
    32     73.8 MiB      0.0 MiB       m = 2
    33     73.8 MiB      0.0 MiB       while m < n ** 2:
    34     73.8 MiB      0.0 MiB           if a[m] != 0:
    35     73.8 MiB      0.0 MiB               j = m *2
    36     73.8 MiB      0.0 MiB               while j < n ** 2:
    37     73.8 MiB      0.0 MiB                   a[j] = 0
    38     73.8 MiB      0.0 MiB                   j = j + m
    39     73.8 MiB      0.0 MiB           m += 1
    40                             
    41     73.8 MiB      0.0 MiB       b = []
    42     73.8 MiB      0.0 MiB       for i in a:
    43     73.8 MiB      0.0 MiB           if a[i] != 0:
    44     73.8 MiB      0.0 MiB               b.append(a[i])
    45                                     
    46     73.8 MiB      0.0 MiB       return(b[n-1])
    

Python 3.6 (интерпритатор Spyder), Windows 10 x64
"""  