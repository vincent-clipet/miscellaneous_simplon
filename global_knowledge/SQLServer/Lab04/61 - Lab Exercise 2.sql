---------------------------------------------------------------------
-- LAB 04
--
-- Exercise 2
---------------------------------------------------------------------

USE TSQL;
GO

---------------------------------------------------------------------
-- Task 1
-- 
--
-- Execute the query exactly as written inside a query window and observe the result.
--
-- You get an error. What is the error message? Why do you think you got this error? 
---------------------------------------------------------------------

SELECT 
	C.custid, C.contactname, O.orderid
FROM Sales.Customers AS C  
INNER JOIN Sales.Orders AS O ON C.custid = O.custid;




---------------------------------------------------------------------
-- Task 2
-- 
-- Notice that there are full source table names written as table aliases. 
--
-- Apply the needed changes to the SELECT statement so that it will run without an error. Test the changes by executing the T-SQL statement.
--
-- Observe and compare the results that you got with the recommended result shown in the file 62 - Lab Exercise 2 - Task 2 Result.txt. 
---------------------------------------------------------------------

SELECT 
	C.custid, C.contactname, O.orderid
FROM Sales.Customers AS C  
INNER JOIN Sales.Orders AS O ON C.custid = O.custid;


---------------------------------------------------------------------
-- Task 3
-- 
-- Copy the T-SQL statement from task 2 and modify it to use the table aliases �C� for the Sales.Custumers table and �O� for the Sales.Orders table.
--
-- Execute the written statement and compare the results with the results in task 2.
--
-- Change the prefix of the columns in the SELECT statement with full source table names and execute the statement.
--
-- You get an error. Why?
--
-- Change the SELECT statement to use the table aliases written at the beginning of the task.
---------------------------------------------------------------------

SELECT 
	C.custid, C.contactname, O.orderid
FROM Sales.Customers AS C  
INNER JOIN Sales.Orders AS O ON C.custid = O.custid;


---------------------------------------------------------------------
-- Task 4
-- 
-- Copy the T-SQL statement from task 3 and modify it to include three additional columns from the Sales.OrderDetails table: productid, qty, and unitprice.
--
-- Execute the written statement and compare the results that you got with the recommended result shown in the file 63 - Lab Exercise 2 - Task 4 Result.txt. 
---------------------------------------------------------------------

SELECT 
	C.custid, C.contactname, O.orderid, OD.productid, OD.qty, OD.unitprice
FROM Sales.Customers AS C  
INNER JOIN Sales.Orders AS O ON C.custid = O.custid
INNER JOIN Sales.OrderDetails AS OD ON O.orderid = OD.orderid

