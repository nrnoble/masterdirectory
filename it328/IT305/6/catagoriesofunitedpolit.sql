SELECT category.category_id, category.name FROM category
INNER JOIN film_category
ON category.category_id = film_category.category_id
WHERE film_category.film_id = '925'