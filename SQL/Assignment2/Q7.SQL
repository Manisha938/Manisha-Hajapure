#7. Write a query to retrieve products where the `product_name` contains "Pro".
SELECT *
FROM Products
WHERE product_name LIKE '%Pro%';