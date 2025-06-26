-- Create the tables

CREATE TABLE Departments (
    ID SERIAL PRIMARY KEY,
    NAME VARCHAR(255) NOT NULL,
    MANAGER_ID INT
);

CREATE TABLE Employees (
    ID SERIAL PRIMARY KEY,
    FIRSTNAME VARCHAR(50) NOT NULL,
    LASTNAME VARCHAR(50) NOT NLL,
    EMAIL VARCHAR(255),
    PHONE_NUMBER VARCHAR(13),
    DEPARTMENT_ID INT,
    FOREIGN KEY (DEPARTMENT_ID) REFERENCES Departments(ID)
);

CREATE TABLE Projects (
    ID SERIAL PRIMARY KEY,
    NAME VARCHAR(255) NOT NULL,
    DESCRIPTION TEXT,
    START_DATE DATE,
    END_DATE DATE
);

-- Inserting values into the tables

INSERT INTO Departments (ID, NAME, MANAGER_ID) 
VALUES (1, 'Finance', 101),
    (2, 'Management', 102),
    (3, 'Human Resource', 103);

INSERT INTO Employees (ID, FIRSTNAME, LASTNAME, EMAIL, PHONE_NUMBER, DEPARTMENT_ID) 
VALUES (11, 'Chioma', 'Ozoko', 'chozoko@gmail.com', '+2547012345678', 1),
    (12, 'Kanyi', 'Jaylah', 'kannyijay@gmail.com', '+254708957854', 2),
    (13, 'Jude', 'Lous', 'jlous@gmail.com', '+254771296963', 3);

INSERT INTO Projects (ID, NAME, DESCRIPTION, START_DATE, END_DATE) 
VALUES (1, 'Website Redesign', 'Revamp company website for modern look', '2025-01-15', '2025-06-30'),
    (2, 'Recruitment Drive', 'Hire 5 new engineers', '2025-02-01', '2025-04-30'),
    (3, 'Product Launch', 'Launch new mobile app', '2025-03-01', '2025-07-15');

-- Updating a table - add a new column to Employee table
ALTER TABLE Employees
ADD COLUMN JOB_TITLE VARCHAR(100);

-- Deleting a table - delete the projects table
DROP TABLE Projects;

-- Removing fields - remove the manager_id field from the departments table
ALTER TABLE Departments
DROP COLUMN MANAGER_ID;