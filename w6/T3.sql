SELECT city, count(account_id) AS count
FROM Accounts
GROUP BY city
HAVING count > 4
ORDER BY city;