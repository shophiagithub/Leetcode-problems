# Write your MySQL query statement below
SELECT IFNULL((SELECT num
FROM MyNumbers 
GROUP BY num
HAVING COUNT(num)<2
ORDER BY num DESC
LIMIT 1),null) AS num;