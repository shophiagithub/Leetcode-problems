WITH cte AS(SELECT tiv_2016,
COUNT(tiv_2015) OVER(
    PARTITION BY tiv_2015
) AS tiv_2015,
COUNT(lat) OVER(
    PARTITION BY lat,lon
) AS location
FROM Insurance)

SELECT ROUND(SUM(tiv_2016),2) AS tiv_2016
FROM cte
WHERE tiv_2015>1 AND location=1;