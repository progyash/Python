create database base3;
use base3;
CREATE TABLE EMPLOYEE (
  empId INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  dept TEXT NOT NULL
);

-- insert
INSERT INTO EMPLOYEE VALUES (0001, 'Yash', 'Sales');
INSERT INTO EMPLOYEE VALUES (0002, 'Aniket', 'Accounting');
INSERT INTO EMPLOYEE VALUES (0003, 'Sahil', 'Sales');

-- fetch 
SELECT * FROM EMPLOYEE;
