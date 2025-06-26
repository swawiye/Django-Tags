# SELECT * FROM database; - Extracts data from a database
# UPDATE: - Updates data in a database(changing the keys and values)
# DELETE: - Deletes data from a database
# DROP DATABSE IF EXISTS name_of_db; - Deletes a database
# INSERT INTO: - Inserts data into a database
# CREATE DATABASE: - Creates a new database
# ALTER DATABASE: - Modify data in a database(change the structure of the database), ex: ALTER DATABASE old_name RENAME TO new_name;
# ALTER TABLE: - Modify data in a table
# CREATE TABLE: - Creates a table
# DELETE: - Deletes data from a table
# DROP TABLE: - Deletes a table and it's contents
# CREATE INDEX: - Creates an index(search key)
# DROP INDEX: - Delete an index(search key)

# Syntax for updating records
# UPDATE Customers
# SET column1= values, column2= values
# WHERE condition;

# Selecting particular records to view
# SELECT * FROM Customers 
# WHERE NAME IN ('Lorna', 'Georgina'); 

# Selecting other records aprt from the chosen ones
# SELECT * FROM Customers 
# WHERE NAME NOT IN ('Lorna', 'Georgina'); 

# Selecting records starting with a particular character
# SELECT * FROM Customers 
# WHERE FIELD LIKE 'K____%';
 
# Selecting records using conditional statements
# SELECT * FROM Customers 
# WHERE (AGE = 32 OR SALARY < 25000) AND (NAME = 'Georgina' OR NAME = 'James');

# Inserting several values
# INSERT INTO Customers (ID, NAME, AGE, ADDRESS, SALARY)
# VALUES (4, 'Victor', 23, 'Kahawa', 24800.00),
#         (5, 'Victoria', 24, 'Kahawe', 27800.00),
#         (6, 'Victorene', 25, 'Kahawi', 29800.00);

# Joining tables
# SELECT ID, NAME, AMOUNT, DATE
# FROM Customers -the primary key here
# INNER JOIN Orders -becomes a foreign key here
# ON Customers.ID = Orders.CUSTOMER_ID;

# Returning all the joined records of two tables
# SELECT ID, NAME, AMOUNT, DATE
# FROM Customers
# LEFT JOIN Orders 
# ON Customers.ID = Orders.CUSTOMER_ID;

# Works the same as left join
# SELECT ID, NAME, AMOUNT, DATE
# FROM Customers
# FULL JOIN Orders 
# ON Customers.ID = Orders.CUSTOMER_ID;

# Only returning all the joined records of two tables, same as the one for joining tables
# SELECT ID, NAME, AMOUNT, DATE
# FROM Customers
# RIGHT JOIN Orders 
# ON Customers.ID = Orders.CUSTOMER_ID;

# Returning all the records from the tables
# SELECT ID, NAME, AMOUNT, DATE
# FROM Customers
# CROSS JOIN Orders; 

