SELECT first_name, last_name, salary FROM employees
WHERE salary > (SELECT AVG (salary) FROM employees);

SELECT first_name, last_name FROM employees e
WHERE salary > (
SELECT avg(salary) FROM employees WHERE department = e.department
);

SELECT * FROM employees;



SELECT department, count(*) as total from employees group by department;

SELECT department, is_active, avg(salary) as total from employees group by department, is_active;

SELECT department, is_active, avg(salary) as total from employees group by department, is_active having total > 53000;

SELECT department, is_active, sum(salary) as total from employees group by department, is_active with rollup;