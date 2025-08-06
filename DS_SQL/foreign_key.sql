CREATE DATABASE school;
USE school;

CREATE TABLE classes (
    class_id INT AUTO_INCREMENT PRIMARY KEY,
    class_name VARCHAR(50) NOT NULL
);

CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL,
    class_id INT,
    FOREIGN KEY (class_id) REFERENCES classes(class_id)
        ON UPDATE CASCADE
        ON DELETE SET NULL
);

INSERT INTO classes (class_name) VALUES ('Mathematics'), ('Science'), ('History');
INSERT INTO students (student_name, class_id) VALUES 
('Alice', 1),
('Bob', 2),
('Charlie', 1);

SELECT * FROM students;
SELECT * FROM classes;

DELETE FROM classes WHERE class_id = 2;

UPDATE classes SET class_id = 101 WHERE class_id = 1;
UPDATE classes SET class_id = 102 WHERE class_id = 2;
UPDATE classes SET class_id = 103 WHERE class_id = 3;

SHOW CREATE TABLE students; 

SELECT 
    table_name, 
    column_name, 
    constraint_name, 
    referenced_table_name, 
    referenced_column_name
FROM 
    information_schema.key_column_usage
WHERE 
    referenced_table_name IS NOT NULL
    AND table_schema = 'school';

