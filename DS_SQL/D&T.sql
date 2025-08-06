-- SELECT current_timestamp();
SELECT NOW();
-- SELECT LOCALTIME/LOCALTIMESTAMP;

-- ALTER TABLE students ADD COLUMN date_joined DATETIME DEFAULT (NOW());
ALTER TABLE students
ADD COLUMN date_joined TIMESTAMP DEFAULT CURRENT_TIMESTAMP;

SELECT * FROM students;

USE raju;
CREATE TABLE college_students (
    roll_no INT PRIMARY KEY,
    age INT CONSTRAINT chk_age CHECK (age >= 5),
    email VARCHAR(100) UNIQUE
);

INSERT INTO college_students VALUES
(1, 22, "raju@gmail.com");

SELECT * FROM college_students;