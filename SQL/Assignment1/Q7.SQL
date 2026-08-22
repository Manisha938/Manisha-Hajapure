#7. Extract the first three characters from the `student_name` column in the `Students` table
SELECT LEFT(student_name, 3) AS first_three_characters
FROM Students;