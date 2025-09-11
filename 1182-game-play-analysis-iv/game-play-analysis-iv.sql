# Write your MySQL query statement below
WITH cte AS(
    SELECT player_id,MIN(event_date) AS first_date
    FROM Activity 
    GROUP BY player_id
)
SELECT ROUND(COUNT(a.player_id)/
(SELECT COUNT(DISTINCT(player_id))
FROM Activity),2) AS fraction
FROM Activity a
JOIN cte c ON a.player_id=c.player_id
AND a.event_date=DATE_ADD(c.first_date,INTERVAL 1 DAY);
