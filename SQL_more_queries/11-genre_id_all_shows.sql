-- Genre ID for all shows
UPDATE tv_show_genres
SET tv_show_genres.genre_id = NULL
WHERE tv_show_genres.genre_id = NULL;
SELECT tv_shows.title, tv_show_genres.genre_id 
FROM tv_shows
JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;

