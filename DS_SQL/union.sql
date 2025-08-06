SELECT * FROM students;

SELECT student_id FROM marks
UNION
SELECT id FROM students;

CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department VARCHAR(50),
    hire_date DATE,
    salary DECIMAL(10, 2),
    is_active BOOLEAN
);

INSERT INTO employees (employee_id, first_name, last_name, department, hire_date, salary, is_active)
VALUES
(1, 'Amit', 'Sharma', 'HR', '2021-01-15', 55000.00, TRUE),
(2, 'Priya', 'Verma', 'Finance', '2020-03-20', 62000.00, TRUE),
(3, 'Rahul', 'Mehta', 'Engineering', '2019-07-12', 75000.00, TRUE),
(4, 'Neha', 'Singh', 'Marketing', '2022-10-05', 48000.00, TRUE),
(5, 'Ravi', 'Kumar', 'Sales', '2021-04-11', 52000.00, TRUE),
(6, 'Sneha', 'Das', 'Engineering', '2018-06-01', 80000.00, FALSE),
(7, 'Deepak', 'Jha', 'HR', '2023-01-18', 50000.00, TRUE),
(8, 'Kiran', 'Chowdhury', 'Finance', '2020-11-30', 61000.00, TRUE),
(9, 'Manish', 'Rao', 'Sales', '2019-05-22', 53000.00, FALSE),
(10, 'Anita', 'Ghosh', 'Engineering', '2017-12-10', 82000.00, TRUE),
(11, 'Suman', 'Roy', 'Marketing', '2023-03-09', 47000.00, TRUE),
(12, 'Jay', 'Patel', 'HR', '2021-09-26', 54000.00, TRUE),
(13, 'Aarti', 'Joshi', 'Sales', '2020-06-14', 51000.00, FALSE),
(14, 'Vinay', 'Reddy', 'Engineering', '2019-08-08', 77000.00, TRUE),
(15, 'Nisha', 'Batra', 'Finance', '2018-02-17', 60000.00, TRUE),
(16, 'Suresh', 'Naik', 'Marketing', '2022-05-30', 49000.00, TRUE),
(17, 'Megha', 'Iyer', 'HR', '2019-10-03', 53000.00, FALSE),
(18, 'Kunal', 'Mitra', 'Sales', '2021-07-21', 56000.00, TRUE),
(19, 'Tina', 'Sen', 'Engineering', '2020-01-05', 78000.00, TRUE),
(20, 'Arjun', 'Pandey', 'Finance', '2023-04-16', 63000.00, TRUE);

CREATE TABLE emp_personal (
    personal_id INT PRIMARY KEY,
    employee_id INT,
    date_of_birth DATE,
    phone_number VARCHAR(15),
    email VARCHAR(100),
    address VARCHAR(200),
    marital_status VARCHAR(10),
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);

INSERT INTO emp_personal (personal_id, employee_id, date_of_birth, phone_number, email, address, marital_status)
VALUES
(1, 1, '1990-05-14', '9876543210', 'amit.sharma@example.com', '123 Sector A, Delhi', 'Married'),
(2, 2, '1988-09-23', '9812345678', 'priya.verma@example.com', '45 Elm St, Mumbai', 'Single'),
(3, 3, '1992-03-11', '9845567890', 'rahul.mehta@example.com', '78 Hill Rd, Pune', 'Single'),
(4, 4, '1995-06-08', '9832145789', 'neha.singh@example.com', '22 Rose Ave, Jaipur', 'Married'),
(5, 5, '1989-07-21', '9801234567', 'ravi.kumar@example.com', '11 Ocean Dr, Kolkata', 'Single'),
(6, 6, '1991-01-30', '9823456789', 'sneha.das@example.com', '301 Palm St, Bengaluru', 'Married'),
(7, 7, '1996-12-05', '9877894561', 'deepak.jha@example.com', '67 Ring Rd, Patna', 'Single'),
(8, 8, '1987-08-27', '9847891234', 'kiran.chowdhury@example.com', '90 Forest Lane, Chandigarh', 'Married'),
(9, 9, '1993-02-16', '9831239876', 'manish.rao@example.com', '15 Skyline Blvd, Hyderabad', 'Single'),
(10, 10, '1985-10-10', '9819876543', 'anita.ghosh@example.com', '89 Coral St, Chennai', 'Married'),
(11, 11, '1998-04-19', '9821345678', 'suman.roy@example.com', '76 Greenway, Lucknow', 'Single'),
(12, 12, '1990-11-11', '9843217890', 'jay.patel@example.com', '33 Maple Ct, Surat', 'Married'),
(13, 13, '1986-06-28', '9874563210', 'aarti.joshi@example.com', '120 Sun St, Agra', 'Single'),
(14, 14, '1991-03-03', '9837896541', 'vinay.reddy@example.com', '209 Moon Ave, Bhopal', 'Married'),
(15, 15, '1989-08-15', '9825698741', 'nisha.batra@example.com', '501 Lotus Rd, Ranchi', 'Single'),
(16, 16, '1994-02-24', '9851239087', 'suresh.naik@example.com', '77 Cloud Ln, Mysuru', 'Married'),
(17, 17, '1992-09-01', '9847981325', 'megha.iyer@example.com', '88 Lake View, Nagpur', 'Single'),
(18, 18, '1990-07-07', '9835632198', 'kunal.mitra@example.com', '63 Crystal St, Noida', 'Married'),
(19, 19, '1987-05-12', '9863218790', 'tina.sen@example.com', '42 Rainbow Rd, Kochi', 'Single'),
(20, 20, '1993-12-14', '9841235987', 'arjun.pandey@example.com', '109 Windmill Blvd, Indore', 'Married');

SELECT email, address FROM emp_personal
UNION
SELECT first_name, last_name FROM employees;
