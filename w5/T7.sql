SELECT name, vitamin, value
FROM Fruit
WHERE name NOT IN (SELECT name FROM Fruit WHERE vitamin = 'Folate (folic acid)')
ORDER BY name desc, vitamin;