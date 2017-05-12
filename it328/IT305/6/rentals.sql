SELECT customer.first_name, customer.last_name
FROM customer
INNER JOIN rental
ON customer.customer_id = rental.customer_id
WHERE rental.rental_date like '2005-05-25%';
