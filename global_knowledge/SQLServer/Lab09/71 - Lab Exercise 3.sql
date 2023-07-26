---------------------------------------------------------------------
-- LAB 09
--
-- Exercise 3
---------------------------------------------------------------------

USE TSQL;
GO

---------------------------------------------------------------------
-- Task 1
-- 
-- A junior analyst prepared a T-SQL statement to retrieve the number of orders
-- and the number of customers for each order year. Observe the provided T-SQL statement
-- and execute it:
--
-- Observe the result and notice that the number of orders is the same as
-- the number of customers. Why?
--
-- Correct the T-SQL statement to show the correct number of customers
-- that placed an order for each year.
--
-- Execute the written statement and compare the results that you got with the recommended
-- result shown in the file 72 - Lab Exercise 3 - Task 1 Result.txt. 
---------------------------------------------------------------------

SELECT
	YEAR(orderdate) AS orderyear,
	COUNT(orderid) AS nooforders,
	COUNT(DISTINCT custid) AS noofcustomers
FROM Sales.Orders 
GROUP BY YEAR(orderdate);

---------------------------------------------------------------------
-- Task 2
-- 
-- Write a SELECT statement to retrieve the number of customers based on the first letter
-- of the values in the contactname column from the Sales.Customers table.
-- Add an additional column to show the total number of orders placed
-- by each group of customers.
-- Use the aliases firstletter, noofcustomers and nooforders.
-- Order the result by the firstletter column.
--
-- Execute the written statement and compare the results that you got with the recommended result shown in the file 73 - Lab Exercise 3 - Task 2 Result.txt.
---------------------------------------------------------------------

SELECT
	SUBSTRING(C.contactname, 0, 2) AS firstletter,
	COUNT(DISTINCT C.custid) AS noofcustomers,
	COUNT(*) AS nooforders
FROM Sales.Customers AS C
LEFT JOIN Sales.Orders AS O ON O.custid = C.custid
GROUP BY SUBSTRING (C.contactname, 0, 2)
ORDER BY SUBSTRING (C.contactname, 0, 2);


---------------------------------------------------------------------
-- Task 3
-- 
-- Copy the T-SQL statement in exercise 1, task 4, and modify to include the following information
-- about for each product category:
-- total sales amount, number of orders, and average sales amount per order.
-- Use the aliases totalsalesamount, nooforders, and avgsalesamountperorder, respectively.
--
-- Execute the written statement and compare the results that you got with the recommended result shown in the file 74 - Lab Exercise 3 - Task 3 Result.txt. 
---------------------------------------------------------------------

SELECT
	PC.categoryid,
	PC.categoryname,
	SUM(OD.qty * OD.unitprice) AS totalsalesamount,
	COUNT(DISTINCT O.orderid) AS nooforders,
	(SUM(OD.qty * OD.unitprice) / COUNT(DISTINCT O.orderid)) AS avgsalesamountperorder
FROM [Production].[Products] AS P
LEFT JOIN [Production].[Categories] AS PC ON PC.categoryid = P.categoryid
LEFT JOIN [Sales].[OrderDetails] AS OD ON OD.productid = P.productid
LEFT JOIN [Sales].[Orders] AS O ON O.orderid = OD.orderid
WHERE YEAR(O.orderdate) = 2008
GROUP BY PC.categoryid, PC.categoryname