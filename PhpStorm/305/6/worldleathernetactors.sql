USE nnoble_sakila;
SELECT actor.first_name, actor.last_name  FROM actor
inner JOIN film_actor
ON film_actor.actor_id = actor.actor_id
WHERE film_actor.film_id ='990';