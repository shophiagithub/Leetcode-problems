# Write your MySQL query statement belo
WITH cte AS (SELECT product_id,MIN(year) AS first_year
FROM Sales
GROUP BY product_id)
SELECT s.product_id,s.year AS first_year,quantity,price 
FROM sales s
INNER JOIN cte c ON s.year=c.first_year AND
s.product_id=c.product_id;