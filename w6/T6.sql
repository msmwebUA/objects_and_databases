SELECT
    DISTINCT(fruit) AS fruit,
    [value] AS amount
FROM Fruits
WHERE vitamin = 'Vitamin C' AND [value] > 5000
ORDER BY fruit;