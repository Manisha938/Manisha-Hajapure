#16. Question:
#You have two tables:
##• Orders with columns: order_id, customer_id, order_date, total_amount.
#• Customers with columns: customer_id, customer_name.
##• O/P- customer_id, customer_name, avg_order_value
#Write an SQL query to find the average order value (total_amount) for each customer. Only
#include customers who have made more than 2 orders.
SELECT 
    c.customer_id,
    c.customer_name,
    AVG(o.total_amount) AS avg_order_value
FROM Customers AS c
INNER JOIN Orders AS o
    ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.customer_name
HAVING COUNT(o.order_id) > 2;