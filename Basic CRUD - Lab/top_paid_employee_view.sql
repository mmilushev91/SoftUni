CREATE VIEW employees_view AS

SELECT 
	*
FROM employees
ORDER BY salary DESC
LIMIT 1;

SELECT * FROM employees_view;
