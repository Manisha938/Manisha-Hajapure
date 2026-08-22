#10. Get the total and average sales amount per category from the `Sales` table, considering only
#categories with total sales greater than 1,00,000.
SELECT category,
       SUM(sales_amount) AS total_sales,
       AVG(sales_amount) AS average_sales
FROM Sales
GROUP BY category
HAVING SUM(sales_amount) > 100000;