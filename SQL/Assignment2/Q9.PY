#9. Write an SQL query to find the number of orders placed in each month of the year.
SELECT 
    MONTH(order_date) AS month,
    COUNT(*) AS total_orders
FROM Orders
GROUP BY MONTH(order_date)
ORDER BY MONTH(order_date);