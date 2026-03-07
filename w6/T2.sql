SELECT city, AVG(balance)
FROM Accounts
GROUP BY city
ORDER BY city;