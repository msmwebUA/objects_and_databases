SELECT FirstName, LastName
FROM Employee
WHERE ReportsTo = (SELECT EmployeeId FROM Employee WHERE LastName = 'Edwards' AND FirstName = 'Nancy')
ORDER BY FirstName, LastName;