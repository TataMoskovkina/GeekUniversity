# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 00:37:41 2018

@author: mosko
"""

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import sys
import shutil

list_new_dirs = [('dir_' + str(i + 1)) for i in range(9)]

def new_dir(path):
    dir_p = os.path.join(os.getcwd(), path)
    try:
        os.mkdir(dir_p)
    except FileExistsError:
        print("Уже существует")

for i in list_new_dirs:
    new_dir(i)

def delete_dir(path):
    dir_p = os.path.join(os.getcwd(), path)
    try:
        os.rmdir(dir_p)
    except FileExistsError:
        print("такой директории не существует")

for i in list_new_dirs:
   delete_dir(i)  
     
# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def dirs_list(main):
    for _ in os.listdir(main):
        print(_)
        
main = os.getcwd()
dirs_list(main)


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def copy_file(origin_file, new_file):
    shutil.copy(origin_file, new_file)
    
origin_file = sys.argv[0]
new_file = origin_file + ".new"

copy_file(origin_file, new_file)

def change_dir(path):
    try:
        os.chdir(path)
        print(os.getcwd())
    except FileExistsError:
        print("такой директории не существует") 
        
    