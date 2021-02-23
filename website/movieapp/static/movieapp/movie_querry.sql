USE movies;

SELECT movie_name AS "Movie Name", movie_release_year AS "Release Year", movie_genre AS Genre, 
	(SELECT concat_ws(" ", director_first_name, director_last_name)  FROM directors
				WHERE director_id=director_id_1) AS Director, 
	IF(director_id_2 IS NULL, "N/A", (SELECT concat_ws(" ", director_first_name, director_last_name)  FROM directors
				WHERE director_id=director_id_2)) AS "Director 2"
FROM movies m JOIN directors d
	ON m.director_id_1 = d.director_id
ORDER BY movie_genre, movie_release_year, movie_name;