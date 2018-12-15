# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 01:11:59 2018

@author: Московкина Наталия 
"""

# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

first_list = [1, 2, 4, 7, 3, 6, 9, 8]
second_list = [(i ** 2) for i in first_list]
print(second_list)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.
 
fruits_1 = ['apple', 'orange', 'peach', 'pear', 'banana']
fruits_2 = ['pear', 'apple', 'mango', 'banana', 'kiwi']
fruits_3 = [i for i in fruits_1 if i in fruits_2]
print(fruits_3)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

numbers_1 = [2, 6, 12, 25, 46, 18, 36, 89, 33, 24, 56, 43, 48, 116, -12, 81]
numbers_2 = [i for i in numbers_1 if i % 3 == 0 and i > 0 and i % 4 != 0]
print(numbers_2)