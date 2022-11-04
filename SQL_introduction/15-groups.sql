-- number by score
SELECT score, count(*) AS NUMBER 
FROM second_table
GROUP BY score 
ORDER BY score DESC;