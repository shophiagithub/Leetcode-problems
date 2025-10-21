# Write your MySQL query statement below
WITH cte1 AS(SELECT accepter_id AS id
FROM RequestAccepted

UNION ALL

SELECT requester_id AS id 
FROM RequestAccepted)

SELECT id,COUNT(id) AS num
FROM cte1
GROUP BY id 
ORDER BY num DESC
LIMIT 1;