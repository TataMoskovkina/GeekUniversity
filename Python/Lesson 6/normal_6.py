# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 23:20:21 2018

@author: mosko
"""

# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


class Person:
    def __init__(self, surname, name, second_name):
        self.surname = surname
        self.name = name
        self.second_name = second_name
    def get_full_name(self):
        return self.surname + ' ' + self.name + ' ' + self.second_name
    def get_initials(self):
        return '{} {}.{}'.format(self.surname, self.name[0], self.second_name[0])

        
class Pupil(Person):
    def __init__(self, surname, name, second_name, mama, papa, school_class):
        Person.__init__(self, surname, name, second_name)
        
        self.school_class = school_class
        self.mama = mama
        self.papa = papa
        
    def get_school_class(self):
        return self.school_class
    
    def get_parents(self):
        return '{} {}'.format(self.mama, self.papa)
        
class Teacher(Person):
    def __init__(self, surname, name, second_name, subject):
        Person.__init__(self, surname, name, second_name)
        self.subject = subject
        
class Classes:
    def __init__(self, class_rooms, teachers):
        self.class_rooms = class_rooms
        self.teachersdict = {t.subject: t for t in teachers}
        

teachers = [Teacher('Ковальчук', 'Инна', 'Викторовна', 'математика'),
            Teacher('Иванцов', 'Максим', 'Юрьевич', 'Обществознание'),
            Teacher('Портнова', 'Зинаида', 'Ивановна', 'История'),
            Teacher('Хрипунова', 'Екатерина', 'Юрьевна', 'Русский язык'),
            Teacher('Жиркова', 'Вера', 'Константиновна', 'Биология'),
            Teacher('Абрамова', 'Татьяна', 'Владимировна', 'Физика')]

classes = [Classes('5-Б', [teachers[0], teachers[3], teachers[2]]),
           Classes('6-А', [teachers[0], teachers[3], teachers[2], teachers[4]]),
           Classes('7-В', [teachers[0], teachers[3], teachers[2],teachers[4],
        teachers[1]]), Classes('8-А', [teachers[0], teachers[3], 
        teachers[2],teachers[4], teachers[1], teachers[5]]), 
        Classes('2-Б', [teachers[0], teachers[3]])]
            
parents = [Person('Ургант', 'Иван', 'Андреевич'),
           Person('Ургант', 'Анастасия', 'Юрьевна'),
           Person('Иванов', 'Виктор', 'Семенович'),
           Person('Иванова', 'Наталия', 'Гергиевна'),
           Person('Белов', 'Алексей', 'Александрович'),
           Person('Белова', 'Валентина', 'Сергеевна'),
           Person('Сидоров', 'Карл', 'Генрихович'),
           Person('Сидорова', 'Галина', 'Петровна'),
           Person('Мутко', 'Виталий', 'Викторович'),
           Person('Мутко', 'Галина', 'Константиновна'),
           Person('Кузнецов', 'Владимир', 'Геннадиевич'),
           Person('Кузнецова', 'Екатерина', 'Андреевна'),
           Person('Андреев', 'Дмитрий', 'Егорович'),
           Person('Андреева', 'Алина', 'Алексеевна'),
           Person('Егоров', 'Антон', 'Сергеевич'),
           Person('Егорова', 'Клавдия', 'Рустамовна'),
           Person('Уткин', 'Юрий', 'Андреевич'),
           Person('Уткина', 'Вероника', 'Ивановна'),
           Person('Андриевский', 'Тарас', 'Венниаминович'),
           Person('Андриевская', 'Татьяна', 'Антоновна'),]       
    
pupils = [Pupil('Ургант', 'Екатерина', 'Ивановна', parents[0], parents[1], classes[0]),
          Pupil('Иванов', 'Петр', 'Викторович', parents[2], parents[3], classes[0]),
          Pupil('Белов', 'Даниил', 'Алексеевич', parents[4], parents[5], classes[1]),
          Pupil('Сидорова', 'Елена', 'Карловна', parents[6], parents[7], classes[1]),
          Pupil('Мутко', 'Инга', 'Витальевна', parents[8], parents[9], classes[2]),
          Pupil('Кузнецов', 'Олег', 'Владимирович', parents[10], parents[11], classes[2]),
          Pupil('Андреева', 'Ангелина', 'Дмитриевна', parents[12], parents[13], classes[3]),
          Pupil('Егоров', 'Евгений', 'Антонович', parents[14], parents[15], classes[3]),
          Pupil('Уткина', 'Диана', 'Юрьевна', parents[16], parents[17], classes[4]),
          Pupil('Андриевский', 'Максим', 'Тарасович', parents[18], parents[19], classes[4])]

print('Все классы школы:')
for i in classes:
    print(i.class_rooms)

cl_pupils = input('Для получения списка учеников в классе введите номер и '
                     'летеру класса,например 1-А: ')
for f in classes:
    if f.class_rooms == cl_pupils:
        print("{} - Ученики: ".format(f.class_rooms))
        for st in pupils:
            print(st.get_initials())

pupil_subj = input('Для получения списка предметов ученика введите ФИО,'
                   'например Иванов Иван Иванович: ')

for f in pupils:
    if pupil_subj == f.get_full_name():
        print('Предметы {} '.format(f.school_class))
        for sub in classes[0].teachersdict.values():
            print(sub.subject) 
        
pupil_parents = input('Для получения информации о родителях ученика введите ФИО,'
                      'например Иванов Иван Иванович: ')

for n in pupils:
    if pupil_parents == n.get_full_name():
        print(n.get_parents())
        
class_teachers = input('Для получения списка учителей в классе введите номер и летеру' 
                'класса,например 1-А: ')
for t in classes:
    if class_teachers == t.class_rooms:
        print('{} - учителя:'.format(t.class_rooms))
        for j in t.teachersdict.values():
            print(j.get_full_name() + ' ' + j.subject)
        


        
