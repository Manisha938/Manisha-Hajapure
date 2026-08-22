#4. Get the total count of customers from each city in the `Customers` table.
SELECT city, COUNT(*) AS total_customers
FROM Customers
GROUP BY city;