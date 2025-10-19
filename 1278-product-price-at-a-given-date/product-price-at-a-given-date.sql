# Write your MySQL query statement below
WITH cte AS(SELECT product_id,new_price,change_date,
ROW_NUMBER() OVER(
    PARTITION BY product_id
    ORDER BY change_date DESC
) AS row_num
FROM Products
WHERE change_date<='2019-08-16')

SELECT p.product_id,
COALESCE(c.new_price,10) AS price 
FROM 
(SELECT DISTINCT(product_id) FROM Products) p
LEFT JOIN cte c 
ON p.product_id=c.product_id AND c.row_num=1;