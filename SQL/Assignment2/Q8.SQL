#8. Fetch the total number of students per course from the `Students` table, only for courses that
#have at least 30 students enrolled.
SELECT course, COUNT(*) AS total_students
FROM Students
GROUP BY course
HAVING COUNT(*) >= 30;