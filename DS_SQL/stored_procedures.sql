delimiter //

create procedure  list_employees()

begin
SELECT * FROM employees;
SELECT first_name FROM employees;
SELECT department From employees;
end //

delimiter ;

call list_employees();


delimiter //

create procedure  get_employee_id(IN emp_id INT)

begin
SELECT * FROM employees where employee_id = emp_id;
SELECT first_name FROM employees;
-- SELECT department From employees;
end //

delimiter ;

call get_employee_id(3);

DROP PROCEDURE IF EXISTS get_employee_id; 