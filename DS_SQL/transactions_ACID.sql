-- SELECT @@autocommit

-- DISABLE
SET autocommit= 0;

-- ENABLE
-- SET autocommit = 1;

SELECT * FROM students;

START TRANSACTION;
UPDATE students SET age = age - 5 where id = 1;
UPDATE students SET age = age + 5 where id = 2;
COMMIT;

SELECT * FROM students;

rollback;

SET autocommit = 1;