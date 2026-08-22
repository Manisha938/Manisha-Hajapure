#5. Fetch the department-wise average salary from the `Employees` table, only for departments
#where the average salary is greater than 50,000.
SELECT dept_id, AVG(salary) AS average_salary
FROM Employees
GROUP BY dept_id
HAVING AVG(salary) > 50000;