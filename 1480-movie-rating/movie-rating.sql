WITH user_counts AS(SELECT u.name,COUNT(m.user_id) AS user_counts
FROM Users u
JOIN MovieRating m
ON u.user_id=m.user_id
GROUP BY m.user_id
ORDER BY user_counts DESC,u.name ASC),

top_user AS(
SELECT name
FROM user_counts
LIMIT 1
),

movie_rating AS(
    SELECT m.title,AVG(mr.rating) AS avg_rating 
    FROM Movies m
    JOIN MovieRating mr
    ON m.movie_id=mr.movie_id
    WHERE MONTH(created_at)='02' AND YEAR(created_at)='2020'
    GROUP BY mr.movie_id
    ORDER BY avg_rating DESC,m.title ASC
),

top_movie AS (
    SELECT title
    FROM movie_rating
    LIMIT 1
)

SELECT name AS results
FROM top_user
UNION ALL
SELECT title AS results
FROM top_movie;


