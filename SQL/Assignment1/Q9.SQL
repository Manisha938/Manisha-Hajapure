9. Write an SQL query to find the total number of orders placed in each month, considering only
#those months where more than 100 orders were placed.
SELECT MONTH(order_date) AS month,
       COUNT(*) AS total_orders
FROM Orders
GROUP BY MONTH(order_date)
HAVING COUNT(*) > 100;