#17. Question:
#You have two tables:
#• Products with columns: product_id, product_name.
#• Sales with columns: sale_id, product_id, sale_date, amount.
#• O/P- product_id | product_name | sales_count
#Write an SQL query to find the number of sales made for each product. Only include products
#with more than 50 sales.#
SELECT 
    p.product_id,
    p.product_name,
    COUNT(s.sale_id) AS sales_count
FROM Products AS p
INNER JOIN Sales AS s
    ON p.product_id = s.product_id
GROUP BY p.product_id, p.product_name
HAVING COUNT(s.sale_id) > 50;