SELECT nnoble_sakila.actor.first_name, nnoble_sakila.actor.last_name  FROM nnoble_sakila.actor
inner JOIN nnoble_sakila.film_actor
ON film_actor.actor_id = actor.actor_id
WHERE film_actor.film_id ='990';