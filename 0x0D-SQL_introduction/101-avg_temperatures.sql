-- Displays the average temperature (Fahrenheit)
-- by city ordered by temperature (descending).

SELECT city, ROUND(AVG(temperature), 4) AS avg_temp
FROM weather_data
GROUP BY city
ORDER BY avg_temperature DESC;
