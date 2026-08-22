#17. Question:
#You have two tables:
#• Books with columns: book_id, author_id, title, price.
#• Sales with columns: sale_id, book_id, sale_date, quantity.
#• O/P- author_id | total_books_sold

#Write an SQL query to find the total number of books sold by each author. Only include authors
#who have sold more than 100 books.
SELECT b.author_id,
       SUM(s.quantity) AS total_books_sold
FROM Books b
INNER JOIN Sales s
ON b.book_id = s.book_id
GROUP BY b.author_id
HAVING SUM(s.quantity) > 100;