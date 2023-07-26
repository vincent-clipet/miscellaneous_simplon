---------------------------------------------------------------------
-- LAB 04
--
-- Exercise 3
---------------------------------------------------------------------

USE TSQL;
GO

---------------------------------------------------------------------
-- Task 1
-- 
-- In order to better understand the needed tasks, you will first write a SELECT statement against the HR.Employees table showing the empid, lastname, firstname, title, and mgrid columns.
--
-- Execute the written statement and compare the results that you got with the recommended result shown in the file 72 - Lab Exercise 3 - Task 1 Result.txt. Notice the values in the mgrid column. The mgrid column is in a relationship with empid column. This is called a self-referencing relationship. 
---------------------------------------------------------------------

SELECT empid, lastname, firstname, title, mgrid FROM HR.Employees





---------------------------------------------------------------------
-- Task 2
-- 
-- Copy the SELECT statement from task 1 and modify it to include additional columns for
-- the manager information (lastname, firstname) using a self-join.
-- Assign the aliases mgrlastname and mgrfirstname, respectively, to distinguish
-- the manager names from the employee names.
--
-- Execute the written statement and compare the results that you got with the recommended result shown in the file 73 - Lab Exercise 3 - Task 2 Result.txt. Notice the number of rows returned.
--
-- Is it mandatory to use table aliases when writing a statement with a self-join? Can you use a full source table name as alias? Please explain.
--
-- Why did you get fewer rows in the T-SQL statement under task 2 compared to task 1?
---------------------------------------------------------------------

SELECT
	E.empid,
	E.lastname,
	E.firstname,
	E.title,
	E.mgrid,
	M.lastname AS 'mgrlastname',
	M.firstname AS 'mgrfirstname'
FROM
	HR.Employees AS E
LEFT JOIN
	HR.Employees as M
ON
	M.empid = E.mgrid
WHERE
	E.mgrid IS NOT NULL

