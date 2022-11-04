-- say my name
SELECT score, count(*)
FROM second_table
GROUP BY name 
ORDER BY score DESC;