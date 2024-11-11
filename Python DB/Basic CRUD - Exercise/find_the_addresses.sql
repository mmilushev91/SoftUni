SELECT 
	id,
	CONCAT(number, ' ', street) AS adress,
	city_id
FROM addresses
WHERE id >= 20;
