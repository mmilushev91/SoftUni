CREATE VIEW view_continents_countries_currencies_details
AS
SELECT
	CONCAT(cont.continent_name, ': ', cont.continent_code) AS continent_details,
	CONCAT(coun.country_name, ' - ', coun.capital, ' - ', area_in_sq_km, ' - ', 'km2') 
		AS country_information,
	CONCAT(curr.description, ' (', curr.currency_code, ')') AS currencies
		
FROM continents AS cont,
	 countries AS coun,
	 currencies AS curr
WHERE 
	cont.continent_code = coun.continent_code 
	AND
	curr.currency_code = coun.currency_code
ORDER BY country_information, 
		 currencies;

SELECT * FROM view_continents_countries_currencies_details;
