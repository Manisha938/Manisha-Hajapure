#5. Retrieve department-wise total salary from the `Employees` table but only include
#departments where the total salary is greater than 2,00,000.
SELECT department, SUM(salary) AS total_salary
FROM Employees
GROUP BY department
HAVING SUM(salary) > 200000;