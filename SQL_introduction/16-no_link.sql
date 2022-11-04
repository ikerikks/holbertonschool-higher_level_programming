-- say my name
SELECT score, name
FROM second_table
GROUP BY name 
ORDER BY score DESC;