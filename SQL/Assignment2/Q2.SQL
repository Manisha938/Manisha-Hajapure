#2. Fetch the top 10 most expensive products from the `Products` table.
SELECT *
FROM Products
ORDER BY price DESC
LIMIT 10;