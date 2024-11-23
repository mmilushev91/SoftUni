SELECT
	capital,
	TRANSLATE(capital, 'áãåçéíñóú', 'aaaceinou')
		AS tranlsated_name
FROM countries;
