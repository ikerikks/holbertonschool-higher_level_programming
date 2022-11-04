-- number by score
SELECT score, number
FROM second_table
ORDER BY number DESC
GROUP BY score;
