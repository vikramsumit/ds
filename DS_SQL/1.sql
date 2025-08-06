create database raju;

SHOW databases;

-- CREATE TABLE students(
-- 	id INT AUTO_INCREMENT PRIMARY KEY,
-- 	name VARCHAR(100) NOT NULL DEFAULT 'no name',
-- 	age INT,
-- 	email VARCHAR(100) unique,
-- 	admission__date date
-- );
USE raju;

CREATE TABLE students (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) NOT NULL DEFAULT 'No Name',
  age INT,
  grade VARCHAR(10),
  date_of_birth DATE
);

-- DROP TABLE students;

INSERT INTO students (id, name , age, grade, date_of_birth) VALUES
(1, 'Ananya Roy', 18, '9th', '2007-03-15'),
(2, 'Rahul Sen', 19, '10th', '2006-07-22'),
(3, 'Priya Das', 17, '9th', '2008-01-10'),
(4, 'Abhishek Ghosh', 20, '10th', '2005-09-05'),
(5, 'Sneha Mukherjee', 18, '9th', '2007-11-18'),
(6, 'Ritwik Banerjee', 21, '10th', '2004-05-30'),
(7, 'Tania Bose', 18, '10th', '2007-04-02'),
(8, 'Aditya Saha', 19, '8th', '2006-12-12'),
(9, 'Moumita Pal', 17, '8th', '2008-08-25'),
(10, 'Arjun Dey', 20, '10th', '2005-06-14'),
(11, 'Neha Karmakar', 18, '9th', '2007-10-19'),
(12, 'Kunal Mitra', 22, '12th', '2003-02-27'),
(13, 'Riya Dasgupta', 17, '10th', '2008-12-05'),
(14, 'Surajit Mondal', 19, '9th', '2006-04-09'),
(15, 'Payel Sinha', 20, '10th', '2005-08-21'),
(16, 'Rajib Biswas', 21, '10th', '2004-01-17'),
(17, 'Shruti Mallick', 18, '11th', '2007-06-23'),
(18, 'Aniket Roy', 19, '10th', '2006-03-03'),
(19, 'Ishita Chatterjee', 17, '11th', '2008-09-11'),
(20, 'Debanjan Sarkar', 20, '10th', '2005-12-29');

SELECT date_of_birth, name FROM students WHERE grade = "10th";
SELECT * FROM students WHERE age > 19;
SELECT * FROM students WHERE age BETWEEN 16 AND 18;
SELECT * FROM students WHERE name NOT LIKE '%ee';
SELECT * FROM students WHERE name LIKE '%ee';
SELECT * FROM students WHERE date_of_birth IS NULL;
SELECT * FROM students 
WHERE date_of_birth IS NOT NULL
ORDER BY date_of_birth DESC;

SELECT * FROM students 
WHERE date_of_birth IS NOT NULL
ORDER BY date_of_birth ASC LIMIT 5,11; 


SELECT * FROM students;

SHOW TABLES;

DESCRIBE students;
-- DESCRIBE student;

ALTER TABLE students ADD COLUMN is_passed BOOL default true;

DESCRIBE students;

ALTER TABLE students MODIFY COLUMN name varchar(50) AFTER is_passed;

DESCRIBE students;

