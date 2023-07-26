---------------------------------------------------------------------
-- LAB 09
--
-- Exercise 1
---------------------------------------------------------------------

USE TSQL;
GO

---------------------------------------------------------------------
-- Task 2
-- 
-- Write a SELECT statement that will return groups of customers that made a purchase.
-- The SELECT clause should include the custid column from the Sales.Orders table
-- and the contactname column from the Sales.Customers table.
-- Group by both columns and filter only the orders from the sales employee
-- whose empid equals five.
--
-- Execute the written statement and compare the results that you got with the desired results shown in the file 52 - Lab Exercise 1 - Task 1 Result.txt.
---------------------------------------------------------------------

SELECT O.custid, C.contactname
FROM [Sales].[Customers] AS C
LEFT JOIN [Sales].[Orders] AS O ON O.custid = C.custid
WHERE O.empid = 5
GROUP BY O.custid, C.contactname



---------------------------------------------------------------------
-- Task 3
-- 
-- Copy the T-SQL statement in task 2 and modify it to include the city column
-- from the Sales.Customers table in the SELECT clause. 
--
-- Execute the query. You will get an error. What is the error message? Why?
--
-- Correct the query so that it will execute properly.
--
-- Execute the query and compare the results that you got with the desired results shown in the file 53 - Lab Exercise 1 - Task 2 Result.txt.
---------------------------------------------------------------------

SELECT O.custid, C.contactname, C.city
FROM [Sales].[Customers] AS C
LEFT JOIN [Sales].[Orders] AS O ON O.custid = C.custid
WHERE O.empid = 5
GROUP BY O.custid, C.contactname, C.city



---------------------------------------------------------------------
-- Task 4
-- 
-- Write a SELECT statement that will return groups of rows based on the custid column
-- and a calculated column orderyear representing the order year
-- based on the orderdate column from the Sales.Orders table.
-- Filter the results to include only the orders from the sales employee
-- whose empid equal five.
--
-- Execute the written statement and compare the results that you got with the desired results shown in the file 54 - Lab Exercise 1 - Task 3 Result.txt.
---------------------------------------------------------------------

SELECT O.custid, year(O.orderdate)
FROM Sales.Orders AS O
WHERE O.empid = 5
GROUP BY O.custid, year(O.orderdate)




---------------------------------------------------------------------
-- Task 5
-- 
-- Write a SELECT statement to retrieve groups of rows based on the categoryname column
-- in the Production.Categories table.
-- Filter the results to include only the product categories that were ordered
-- in the year 2008.
--
-- Execute the written statement and compare the results that you got with the desired results shown in the file 55 - Lab Exercise 1 - Task 4 Result.txt. 
---------------------------------------------------------------------


SELECT PC.categoryid, PC.categoryname
FROM [Production].[Products] AS P
LEFT JOIN [Production].[Categories] AS PC ON PC.categoryid = P.categoryid
LEFT JOIN [Sales].[OrderDetails] AS OD ON OD.productid = P.productid
LEFT JOIN [Sales].[Orders] AS O ON O.orderid = OD.orderid
WHERE YEAR(O.orderdate) = 2008
GROUP BY PC.categoryid, PC.categoryname