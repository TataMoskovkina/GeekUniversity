--1. Реализовать практические задания на примере других таблиц и запросов.

--Для начала я добавлю еще несколько отделов в таблицу departments(у меня всего 9 отделов, маловато будет):

set autocommit=0;
start transaction;
insert into departments (dept_no, dept_name) value ('d011', 'C');
insert into departments (dept_no, dept_name) value ('d012', 'С#');
insert into departments (dept_no, dept_name) value ('d013', 'Processing');
insert into departments (dept_no, dept_name) value ('d014', 'Analitics');

commit;

--Теперь удалим из таблицы titles сотрудников с должностью "Staff"  и не забудем отменить это действие командой rollback:

set autocommit=0;
start transaction;
delete from titles where titles.title = 'Staff';

rollback;

--Добавим во вновь созданные отделы сотрудников, назначим менеджеров.

set autocommit=0;
start transaction;
insert into employees (emp_no, birth_date, first_name, last_name, gender, hire_date) value (500001, '1967-01-25', 'Hermiona', 'Grainger', 'F', '2018-12-17');
insert into employees (emp_no, birth_date, first_name, last_name, gender, hire_date) value (500002, '1980-05-16', 'Tom', 'Reddle', 'M', '2018-12-17');
insert into employees (emp_no, birth_date, first_name, last_name, gender, hire_date) value (500003, '1978-03-06', 'Anthony', 'Hoplins', 'M', '2018-12-17');
insert into employees (emp_no, birth_date, first_name, last_name, gender, hire_date) value (500004, '1985-06-11', 'Molly', 'Malone', 'F', '2018-12-17');
insert into employees (emp_no, birth_date, first_name, last_name, gender, hire_date) value (500005, '1990-07-24', 'Ginevra', 'Wisley', 'F', '2018-12-17');
insert into employees (emp_no, birth_date, first_name, last_name, gender, hire_date) value (500006, '1971-09-13', 'Albus', 'Dambldore', 'M', '2018-12-17');
insert into employees (emp_no, birth_date, first_name, last_name, gender, hire_date) value (500007, '1982-02-20', 'Bulavina', 'Ekaterina', 'F', '2018-12-17');
insert into employees (emp_no, birth_date, first_name, last_name, gender, hire_date) value (500008, '1986-05-08', 'Ivanov', 'Ivan', 'M', '2018-12-17');

commit;

set autocommit=0;
start transaction;

insert into dept_emp (emp_no, dept_no, from_date, to_date) value (500001, 'd011', '2018-12-17', '9999-01-01');
insert into dept_emp (emp_no, dept_no, from_date, to_date) value (500002, 'd011', '2018-12-17', '9999-01-01');
insert into dept_emp (emp_no, dept_no, from_date, to_date) value (500003, 'd012', '2018-12-17', '9999-01-01');
insert into dept_emp (emp_no, dept_no, from_date, to_date) value (500004, 'd012', '2018-12-17', '9999-01-01');
insert into dept_emp (emp_no, dept_no, from_date, to_date) value (500005, 'd013', '2018-12-17', '9999-01-01');
insert into dept_emp (emp_no, dept_no, from_date, to_date) value (500006, 'd013', '2018-12-17', '9999-01-01');
insert into dept_emp (emp_no, dept_no, from_date, to_date) value (500007, 'd014', '2018-12-17', '9999-01-01');
insert into dept_emp (emp_no, dept_no, from_date, to_date) value (500008, 'd014', '2018-12-17', '9999-01-01');

commit;

--обозначим их должности

set autocommit=0;
start transaction;

insert into titles (emp_no, title, from_date, to_date) value (500001, 'Senior Engeneer','2018-12-17', '9999-01-01');
insert into titles (emp_no, title, from_date, to_date) value (500002, 'Engeneer','2018-12-17', '9999-01-01');
insert into titles (emp_no, title, from_date, to_date) value (500003, 'Senior Engeneer','2018-12-17', '9999-01-01');
insert into titles (emp_no, title, from_date, to_date) value (500004, 'Engeneer','2018-12-17', '9999-01-01');
insert into titles (emp_no, title, from_date, to_date) value (500005, 'Lead Processing Manager','2018-12-17', '9999-01-01');
insert into titles (emp_no, title, from_date, to_date) value (500006, 'Processing Manager','2018-12-17', '9999-01-01');
insert into titles (emp_no, title, from_date, to_date) value (500007, 'Lead Analyst','2018-12-17', '9999-01-01');
insert into titles (emp_no, title, from_date, to_date) value (500008, 'Analyst','2018-12-17', '9999-01-01');

commit;

--назначим менеджеров.

set autocommit=0;
start transaction;

insert into dept_manager (dept_no, emp_no, from_date, to_date) value ('d011', 500001, '2018-12-17', '9999-01-01');
insert into dept_manager (dept_no, emp_no, from_date, to_date) value ('d012', 500003, '2018-12-17', '9999-01-01');
insert into dept_manager (dept_no, emp_no, from_date, to_date) value ('d012', 500005, '2018-12-17', '9999-01-01');
insert into dept_manager (dept_no, emp_no, from_date, to_date) value ('d014', 500007, '2018-12-17', '9999-01-01');

commit;

-- а теперь переименуем отдел аналитики и соответственно должности.

set autocommit=0;
start transaction;

update departments set dept_name = 'Machine Learning' where dept_no = 'd014';
update titles set title = 'Senior Machine Learning Engineer' where emp_no = 500007;
update titles set title = 'Machine Learning Engineer' where emp_no = 500008;

commit;

2. Проанализировать несколько запросов с помощью EXPLAIN.
Для анализа я взяла запросы из ДЗ_3.

EXPLAIN SELECT CONCAT (e.first_name,',',last_name) AS full_name, MAX(salary) max_salary
FROM salaries s
LEFT JOIN employees e
ON s.emp_no = e.emp_no
GROUP BY full_name;

+----+-------------+-------+------------+--------+---------------+---------+---------+--------------------+---------+----------+-----------------+
| id | select_type | table | partitions | type   | possible_keys | key     | key_len | ref                | rows    | filtered | Extra           |
+----+-------------+-------+------------+--------+---------------+---------+---------+--------------------+---------+----------+-----------------+
|  1 | SIMPLE      | s     | NULL       | ALL    | NULL          | NULL    | NULL    | NULL               | 2730741 |   100.00 | Using temporary |
|  1 | SIMPLE      | e     | NULL       | eq_ref | PRIMARY       | PRIMARY | 4       | employees.s.emp_no |       1 |   100.00 | NULL            |
+----+-------------+-------+------------+--------+---------------+---------+---------+--------------------+---------+----------+-----------------+

EXPLAIN SELECT COUNT(dept_emp.emp_no) AS emp_cnt, SUM(s.salary) AS total_salary, d.dept_name
FROM dept_emp
LEFT JOIN salaries s
ON dept_emp.emp_no = s.emp_no
LEFT JOIN departments d
ON dept_emp.dept_no = d.dept_no
WHERE dept_emp.to_date > now()
AND s.to_date > now()
GROUP BY d.dept_name
ORDER BY emp_cnt;

+----+-------------+----------+------------+--------+-------------------+---------+---------+----------------------------+--------+----------+----------------------------------------------+
| id | select_type | table    | partitions | type   | possible_keys     | key     | key_len | ref                        | rows   | filtered | Extra                                        |
+----+-------------+----------+------------+--------+-------------------+---------+---------+----------------------------+--------+----------+----------------------------------------------+
|  1 | SIMPLE      | dept_emp | NULL       | ALL    | PRIMARY,emp_no    | NULL    | NULL    | NULL                       | 331143 |    33.33 | Using where; Using temporary; Using filesort |
|  1 | SIMPLE      | d        | NULL       | eq_ref | PRIMARY,dept_name | PRIMARY | 16      | employees.dept_emp.dept_no |      1 |   100.00 | NULL                                         |
|  1 | SIMPLE      | s        | NULL       | ref    | PRIMARY,emp_no    | PRIMARY | 4       | employees.dept_emp.emp_no  |      9 |    33.33 | Using where                                  |
+----+-------------+----------+------------+--------+-------------------+---------+---------+----------------------------+--------+----------+----------------------------------------------+

EXPLAIN SELECT AVG(s.salary) avg_salary, d.dept_name 
FROM dept_emp de 
LEFT JOIN departments d 
ON de.dept_no = d.dept_no 
LEFT JOIN salaries s 
ON de.emp_no = s.emp_no
GROUP BY d.dept_name
ORDER BY avg_salary;

+----+-------------+-------+------------+--------+-------------------+---------+---------+----------------------+--------+----------+----------------------------------------------+
| id | select_type | table | partitions | type   | possible_keys     | key     | key_len | ref                  | rows   | filtered | Extra                                        |
+----+-------------+-------+------------+--------+-------------------+---------+---------+----------------------+--------+----------+----------------------------------------------+
|  1 | SIMPLE      | de    | NULL       | index  | NULL              | emp_no  | 4       | NULL                 | 331143 |   100.00 | Using index; Using temporary; Using filesort |
|  1 | SIMPLE      | d     | NULL       | eq_ref | PRIMARY,dept_name | PRIMARY | 16      | employees.de.dept_no |      1 |   100.00 | NULL                                         |
|  1 | SIMPLE      | s     | NULL       | ref    | PRIMARY,emp_no    | PRIMARY | 4       | employees.de.emp_no  |      9 |   100.00 | NULL                                         |
+----+-------------+-------+------------+--------+-------------------+---------+---------+----------------------+--------+----------+----------------------------------------------+

3. Deadlock

Действуя инструкции в методичке получила взаимную блокировку. 

Открыла сначала одно окно терминала и выбрала базу employees, затем открыала второе онко терминала и выбрала такую же базу.
Во втором окне закрыла таблицу из первого окна LOCK TABLE employees READ; и выполнила запрос на выборку.
Затем в первом окне выполнила тот же запрос на выборку, все прошло успешно.
Но при попфтке внести нового сотрудника в таблицу все зависло, пока я не набрала во втором окне команду UNLOCK TABLES;
После этого в первом окне добавление нового сотрудника благополучно заершилось.