# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 01:29:43 2019

@author: moskovkina
"""
import timeit
import random
import copy

def selection_sort(orig_list):
    for i in range(len(orig_list)):
        idx_min = i
        for j in range(i+1, len(orig_list)):
            if orig_list[j] < orig_list[idx_min]:
                idx_min = j
        tmp = orig_list[idx_min]
        orig_list[idx_min] = orig_list[i]
        orig_list[i] = tmp   
    return orig_list    


def insertion_sort(orig_list):
    for i in range(len(orig_list)):
        v = orig_list[i]
        j = i
        while (orig_list[j-1] > v and j > 0):
            orig_list[j] = orig_list[j-1]
            j -= 1
        orig_list[j] = v
    return orig_list   
 

def bubble_sort(orig_list):
    n = 1
    while n < len(orig_list):
        for i in range(len(orig_list)-n):
            if orig_list[i] > orig_list[i+1]:
                orig_list[i], orig_list[i+1] = orig_list[i+1], orig_list[i]
        n +=1
    return orig_list

def quick_sort(orig_list):
    if len(orig_list) <= 1:
        return orig_list
    
    else:
        pivot = random.choice(orig_list)
        less = [x for x in orig_list if x < pivot]
        equal = [x for x in orig_list if x == pivot]
        greater = [x for x in orig_list if x > pivot]    
        return quick_sort(less) + equal + quick_sort(greater)
    

new_list = [random.randint(0, 200) for i in range(10)]
new_list1 = copy.deepcopy(new_list)
new_list2 = copy.deepcopy(new_list)
new_list3 = copy.deepcopy(new_list)

print(new_list)
print(selection_sort(new_list))
print(timeit.timeit("selection_sort(new_list)", setup="from __main__ import selection_sort, new_list", number=100))

print(new_list1)
print(insertion_sort(new_list1))
print(timeit.timeit("insertion_sort(new_list1)", setup="from __main__ import insertion_sort, new_list1", number=100)) 

print(new_list2)
print(bubble_sort(new_list2))
print(timeit.timeit("bubble_sort(new_list2)", setup="from __main__ import bubble_sort, new_list2", number=100))

print(new_list3)
print(quick_sort(new_list3))
print(timeit.timeit("quick_sort(new_list3)", setup="from __main__ import quick_sort, new_list3", number=100))

"""
Время выполнения сортировок:
    Сортировка выбором:
        [0, 3, 5, 1, 2, 4, 2, 3, 34, 34, 16]
        [0, 1, 2, 2, 3, 3, 4, 5, 16, 34, 34]
         0.0012469827083805285
         
    Сортировка вставками:
        [0, 3, 5, 1, 2, 4, 2, 3, 34, 34, 16]
        [0, 1, 2, 2, 3, 3, 4, 5, 16, 34, 34]
        0.0002569755442891619
        
    Пузырьковая сортировка:
        [0, 3, 5, 1, 2, 4, 2, 3, 34, 34, 16]
        [0, 1, 2, 2, 3, 3, 4, 5, 16, 34, 34]
        0.0011546136188371747
        
    Быстрая сортировка:
        [0, 3, 5, 1, 2, 4, 2, 3, 34, 34, 16]
        [0, 1, 2, 2, 3, 3, 4, 5, 16, 34, 34]
        0.0022476478447970294
        
Похоже что быстрая сортировка вообще не быстрая, по крайней мере на маленьком массиве.
Лучший результат показала сортировка вставками.
Ну а сортировку Шелла мой комп похоже не потянул, окончания работы я так и не дождалась.

Попробуем увеличить массив. 
Сам массив и результат сортировки выводить не буду для экономии места.

 Время выполнения сортировок:
    Сортировка выбором:
        0.051941033783805324
         
    Сортировка вставками:
        0.001604616875283682
        
    Пузырьковая сортировка:
        0.051379319192164985
        
    Быстрая сортировка:
        0.02367885557077898
        
И опять быстрая сортировка проиграла в скорости выполнения. 
Все же сортировка вставками оказалась быстрее и на более крупном массиве.

Прогнала также на размере массива 1000. 
Как и при размере массива 100 сортировка вставками наиболее быстрая - 0.026776377987062006.
На втором месте по скорости быстрая сортировка - 0.17145281972443627 
(при этом на маленьком массиве она самая медленная).

А вот третье и четвертое место тут тоже интересная штука.
На массиве в 100 элементов третье место у пузырьковой сортировки (при совсем небольшом преимуществе).
На массиве в 1000 элементов пузырьковая сортировка - 6,328764484479507 оказалась наименее быстрой и
проиграла сортировке выбором - 5.9965669488401545 почти пол секунды.
Сортировка вставками - 0,1407389132418757
Быстрая сортировка - 0.20792084679578693 

Если сравнить пузырьковую сортировку и сортировку вставками по времени выполнения, 
то разница колоссальная, конечно. Я не поленилась и посчитала :) Разница в 44 раза.
"""        
    