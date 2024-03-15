-- Displays the max temperature of each state (ordered by State name).

SELECT state, MAX(temperature) AS max_temp
FROM weather_data
GROUP BY state
ORDER BY state;
