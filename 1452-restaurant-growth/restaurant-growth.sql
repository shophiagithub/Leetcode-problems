# Write your MySQL query statement below
WITH cte1 AS(SELECT visited_on,SUM(amount) AS amount
FROM Customer
GROUP BY visited_on),

cte2 AS(SELECT visited_on,
SUM(amount) OVER(
    ROWS BETWEEN 6 PRECEDING AND CURRENT ROW   
) AS amount,
ROUND(AVG(amount) OVER(
ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
),2) AS average_amount,
RANK() OVER(
   ORDER BY visited_on
) rank_num
FROM cte1
ORDER BY visited_on)

SELECT visited_on,amount,average_amount
FROM cte2
WHERE rank_num>=7;