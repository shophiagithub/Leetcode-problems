# Write your MySQL query statement below
DELETE 
FROM Person 
WHERE id NOT IN(
    SELECT id_keep
    FROM(
    SELECT MIN(id) AS id_keep
    FROM Person 
    GROUP BY email) AS temp
) 