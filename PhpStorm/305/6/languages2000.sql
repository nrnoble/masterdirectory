Select GROUP_CONCAT(DISTINCT language.name)
FROM language
INNER JOIN film
ON language.language_id = film.language_id
WHERE film.release_year = '2000';
