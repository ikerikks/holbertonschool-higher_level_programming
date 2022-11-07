-- Cities by States
SELECT cities.id, cities.name, states.name FROM cities
ORDER BY cities.id;
JOIN states ON cities.name = states.name
