1. Создать VIEW на основе запросов, которые вы сделали в ДЗ к уроку 3.
Найти количество сотрудников в отделах и посмотреть, сколько всего денег получает отдел.
	
CREATE VIEW count_emp_salary 
AS SELECT d.dept_name AS 'Отдел',
COUNT(dept_emp.emp_no) AS 'Количество сотрудников в отделе', 
SUM(s.salary) AS 'Сумма зарплат в отделе'
FROM dept_emp
LEFT JOIN salaries as s
ON dept_emp.emp_no = s.emp_no
LEFT JOIN departments as d
ON dept_emp.dept_no = d.dept_no
WHERE dept_emp.to_date > now()
AND s.to_date > now()
GROUP BY d.dept_name
ORDER BY 'Отдел';

Выбрать среднюю зарплату по отделам.

CREATE VIEW avg_salary_in_dept
AS SELECT AVG(s.salary) AS 'Средняя ЗП в отделе', d.dept_name AS 'Отдел'
FROM dept_emp de 
LEFT JOIN departments d 
ON de.dept_no = d.dept_no 
LEFT JOIN salaries s 
ON de.emp_no = s.emp_no
GROUP BY d.dept_name
ORDER BY 'Средняя ЗП в отделе';

USE geodata

CREATE VIEW moscow_area_cities
AS SELECT cities.id, cities.title AS 'Город', 
regions.title AS 'Регион'
FROM _cities cities 
LEFT JOIN _regions as regions
ON regions.id = cities.region_id 
WHERE regions.title = 'Московская область' LIMIT 10;

2. Создать функцию, которая найдет менеджера по имени и фамилии.

DELIMITER //
CREATE FUNCTION find_emp (first_name varchar(20), last_name varchar(20))
RETURNS varchar(50) DETERMINISTIC
BEGIN
	RETURN (
		SELECT CONCAT(e.first_name, ' ', e.last_name)
		FROM dept_manager as dm
		LEFT JOIN employees as e
		ON e.emp_no = dm.emp_no
		WHERE dm.dept_no = (
			SELECT de.dept_no 
			FROM dept_emp as de
			LEFT JOIN employees as e
			ON de.emp_no = e.emp_no
			WHERE e.first_name = first_name and e.last_name = last_name)
			LIMIT 1
			);
end //


3. Создать триггер, который при добавлении нового сотрудника будет выплачивать ему вступительный бонус, занося запись об этом в таблицу salary.

DELIMITER //
CREATE TRIGGER update_salary AFTER INSERT ON employees
FOR EACH ROW
BEGIN
	INSERT INTO salaries SET emp_no=new.emp_no, alary=20000, from_date=now(), to_date=now();
END //