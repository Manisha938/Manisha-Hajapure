#4. Write a query to count the number of employees in each department from the `Employees`
#table.
SELECT dept_id, COUNT(*) AS employee_count
FROM Employees
GROUP BY dept_id;