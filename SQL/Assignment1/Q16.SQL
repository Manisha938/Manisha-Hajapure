#16. Question:
#You have two tables:
#• Orders with columns: order_id, customer_id, order_date, total_amount.
#• Customers with columns: customer_id, region.
#• O/P- region | total_orders
#Write an SQL query to find the total order amount (total_amount) for each region. Only include
#regions where the total order amount is greater than 10000
SELECT c.region,
       SUM(o.total_amount) AS total_orders
FROM Orders o
INNER JOIN Customers c
ON o.customer_id = c.customer_id
GROUP BY c.region
HAVING SUM(o.total_amount) > 10000;