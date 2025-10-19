# Write your MySQL query statement below
WITH cte AS(SELECT person_name,
SUM(weight) OVER(
    ORDER BY turn 
) AS cumulative_weight, 
LAST_VALUE(turn) OVER(
    ORDER BY turn 
) last_turn,turn
FROM Queue)

SELECT person_name
FROM cte
WHERE cumulative_weight<=1000
ORDER BY turn DESC
LIMIT 1;