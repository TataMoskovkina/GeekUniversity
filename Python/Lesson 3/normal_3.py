# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 18:05:56 2018

@author: Московкина Н.А.
"""
# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1


def fibonacci(n, m):
    f1, f2 = 1, 1
    fib_list = []
    i = 2
    while i < m:
        if i >= n:
            fib_sum = f2 + f1
            f1 = f2
            f2 = fib_sum
            fib_list.append(fib_sum)
            i += 1
        else:
            fib_sum = f2 + f1
            f1 = f2
            f2 = fib_sum
            i += 1
    return fib_list

print(fibonacci(3, 15))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    i = 0
    a = 0
    cnt = 0
    list_size = len(origin_list)
    if list_size == 0:
        return 0
    while i < list_size:
        if (i + 1) != list_size and origin_list[i] > origin_list[i + 1]:
           a = origin_list[i]
           origin_list[i] = origin_list[i + 1]
           origin_list[i + 1] = a
           cnt = 1
        i += 1
        if i == list_size and cnt == 1:
            cnt = 0
            i = 0
    return origin_list

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def fil(fun, a):
    for i in a:
        if fun(a[i]) == True:
            return a[i]
        else:
            continue

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
            
import math

A1, A2, A3, A4 = (4, 7), (1, 3), (8, 5), (9, 6)

def parall(a, b, c, d):
    
    sv1 = False
    sv2 = False
    
    ab = math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)
    cb = math.sqrt((b[0] - c[0])**2 + (b[1] - c[1])**2)
    cd = math.sqrt((d[0] - c[0])**2 + (d[1] - c[1])**2)
    ad = math.sqrt((d[0] - a[0])**2 + (d[1] - a[1])**2)
    
    if ab == cd and cb == ad:
        sv1 = True
        
    hO1 = ((a[0] + c[0])/2, (a[1] + c[1])/2)
    hO2 = ((b[0] + d[0])/2, (b[1] + d[1])/2)
    
    if hO1 == hO2:
        sv2 = True
            
    if sv1 and sv2:
        print("Параллелограм")
    else:
        print("Не параллелограм")
        
parall(A1, A2, A3, A4)
            
            
            
            
            
            