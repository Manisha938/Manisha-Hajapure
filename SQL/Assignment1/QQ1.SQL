#Retrieve the top 5 highest-paid employees from the `Employees` table.
select * from employee
order by salary desc limit 5;
