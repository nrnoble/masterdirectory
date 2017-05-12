SELECT film.title, language.name FROM film
inner JOIN language
ON film.language_id = language.language_id;
