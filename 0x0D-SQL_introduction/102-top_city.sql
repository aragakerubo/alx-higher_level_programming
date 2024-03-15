-- Displays the top 3 of cities temperature
-- during July and August ordered by temperature (descending)

SELECT city, ROUND(AVG(temperature), 4) AS avg_temp
FROM weather_data
WHERE month IN ('07', '08')
GROUP BY city
HAVING COUNT(city) = 2
ORDER BY avg_temperature DESC
LIMIT 3;
