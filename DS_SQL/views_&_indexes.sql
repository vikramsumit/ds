CREATE view raju as SELECT first_name,department,salary, ROUND(DATEDIFF(NOW(), hire_date)/365, 0) as years from employees;
CREATE OR REPLACE view raju as SELECT first_name,last_name,department,salary, ROUND(DATEDIFF(NOW(), hire_date)/365, 0) as years from employees;

SELECT * FROM raju;

USE rajujoins;
SELECT * FROM employees WHERE department = "Engineering" AND is_active = 1;

-- CREATE INDEX idx on employees(department);
-- DROP INDEX idx on employees;

SHOW INDEX FROM employees;