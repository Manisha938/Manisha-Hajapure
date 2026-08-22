#6. Extract only the last four characters of the `phone_number` column and first three characters
#from `customerName` columns from the `Customers` table.
SELECT 
    RIGHT(phone_number, 4) AS last_four_digits,      #gets the last 4 characters of the phone number.
    LEFT(customerName, 3) AS first_three_characters  #gets the first 3 characters of the customer name.
FROM Customers;