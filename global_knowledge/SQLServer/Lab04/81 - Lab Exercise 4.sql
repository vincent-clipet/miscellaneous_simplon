---------------------------------------------------------------------
-- LAB 04
--
-- Exercise 4
---------------------------------------------------------------------

USE TSQL;
GO

---------------------------------------------------------------------
-- Task 1
-- 
--
-- Write a SELECT statement to retrieve
-- custid and contactname columns from the Sales.Customers table
-- orderid column from the Sales.Orders tabl
-- The statement should retrieve all rows from the Sales.Customers table.
--
-- Execute the written statement and compare the results that you got with the recommended result shown in the file 82 - Lab Exercise 4 - Task 1 Result.txt. 
--
-- Notice the values in the column orderid. Are there any missing values (marked as NULL)? Why? 
---------------------------------------------------------------------

SELECT
	C.custid,
	C.contactname,
	O.orderid
FROM
	[Sales].[Customers] AS C
LEFT JOIN
	[Sales].[Orders] AS O
ON
	C.custid = O.custid





