USE college;

CREATE TABLE Supplier (
    Sup_No VARCHAR(5) PRIMARY KEY,
    Sup_Name VARCHAR(50),
    Item_Supplied VARCHAR(50),
    Item_Price INT,
    City VARCHAR(50)
);

INSERT INTO Supplier (Sup_No, Sup_Name, Item_Supplied, Item_Price, City) VALUES
('S1', 'Suresh',   'Keyboard',  400,  'Hyderabad'),
('S2', 'Kiran',    'Processor', 350,  'Delhi'),
('S3', 'Mohan',    'Mouse',     300,  'Delhi'),
('S4', 'Ramesh',   'Processor', 9000, 'Bangalore'),
('S5', 'Manish',   'Printer',   5000, 'Mumbai'),
('S6', 'Srikanth', 'Processor', 8500, 'Chennai');

SELECT * FROM Supplier;

-- Write SQL query to display Supplier numbers and Supplier names whose name starts with ‘R’.
SELECT Sup_No, Sup_Name 
FROM Supplier 
WHERE Sup_Name LIKE 'R%';

-- Write SQL query to display the name of suppliers who supply Processors and whose city is Delhi.
SELECT Sup_No, Sup_Name 
FROM Supplier 
WHERE Item_Supplied = 'Processor' AND City = 'Delhi';

-- Write SQL query to display the names of suppliers who supply the same items as supplied by Ramesh.
SELECT Sup_Name 
FROM Supplier 
WHERE Item_Supplied = (
    SELECT Item_Supplied 
    FROM Supplier 
    WHERE Sup_Name = 'Ramesh'
);

-- Write Sql queries to increase the price of leyboard by 200.
UPDATE Supplier  
SET Item_Price = Item_Price + 200  
WHERE Item_Supplied = 'Keyboard';

SELECT * FROM Supplier;

-- Write SQL query to add a new column called CONTACTNO.
ALTER TABLE Supplier 
ADD CONTACTNO VARCHAR(15);

--Write SQL query to add a new column called CONTACTNO.
SHOW COLUMNS FROM Supplier LIKE 'CONTACTNO';

-- Write SQL query to delete the record whose item price is the lowest of all the items supplied.
DELETE FROM Supplier 
WHERE Item_Price = (
    SELECT min_price FROM (
        SELECT MIN(Item_Price) AS min_price FROM Supplier
    ) AS temp
);

SELECT * FROM supplier;
    
-- Create a view on the table which displays only supplier numbers and supplier names.
CREATE VIEW SupplierView AS 
SELECT Sup_No, Sup_Name 
FROM Supplier;

SELECT * FROM SupplierView;


-- Write SQL query to display the records in the descending order of itemprice for each itemsupplied.
SELECT * 
FROM Supplier 
ORDER BY Item_Supplied DESC;

-- Write SQL query to display the records of suppliers who supply items other than Processor or Keyboard.
SELECT * 
FROM Supplier 
WHERE Item_Supplied NOT IN ('Processor', 'Keyboard');

