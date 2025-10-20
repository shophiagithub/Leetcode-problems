# Write your MySQL query statement below
WITH cte AS(SELECT 
CASE
WHEN income<20000 THEN 'Low Salary'
WHEN income BETWEEN 20000 AND 50000 THEN 'Average Salary'
WHEN income>50000 THEN 'High Salary'
END AS category
FROM Accounts),

counts AS(
    SELECT category,
COUNT(category) AS accounts_count
FROM cte
GROUP BY category
)

SELECT c.category,COALESCE(counts.accounts_count,0) AS accounts_count 
FROM(
  SELECT 'Low Salary' AS category
  UNION ALL
  SELECT 'Average Salary'
  UNION ALL
  SELECT 'High Salary'
) AS c
LEFT JOIN counts ON c.category=counts.category;
