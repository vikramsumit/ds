USE raju;
UPDATE students SET grade='X' where grade='10th';
UPDATE students SET age = age + 1 where age <19 ;
SELECT * FROM students;

DELETE FROM students
WHERE id = 2;
DELETE FROM students
WHERE grade = '9th';
DELETE FROM student
WHERE age < 16;

-- delete all
-- DELETE FROM student;