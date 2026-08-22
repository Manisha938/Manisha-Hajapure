#10. Get the highest and lowest salary per department from the `Employees` table.
SELECT 
    department,
    MAX(salary) AS highest_salary,
    MIN(salary) AS lowest_salary
FROM Employees
GROUP BY department;