
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| bcssy              |
| compny             |
| demo               |
| google             |
| hdfc               |
| hospitales         |
| information_schema |
| manisha            |
| may_apr_2026       |
| my_clg             |
| mysql              |
| performance_schema |
| school             |
| skillected         |
| start_new_batch    |
| student            |
| student123         |
| student_record     |
| university         |
| whatsaap           |
+--------------------+
20 rows in set (0.01 sec)

mysql> use may_apr_2026;
Database changed
mysql> create table employee(id int,name varchar(25),salary decimal(7,2),age int,gender char(3),city varchar(25));
ERROR 1050 (42S01): Table 'employee' already exists
mysql> create table student(id int,name varchar(25),salary decimal(7,2),age int,gender char(3),city varchar(25));
Query OK, 0 rows affected (0.15 sec)

mysql> show tables;
+------------------------+
| Tables_in_may_apr_2026 |
+------------------------+
| department             |
| employee               |
| student                |
+------------------------+
3 rows in set (0.00 sec)

mysql> desc employee;
+---------+--------------+------+-----+----------+-------+
| Field   | Type         | Null | Key | Default  | Extra |
+---------+--------------+------+-----+----------+-------+
| id      | int          | NO   | PRI | NULL     |       |
| name    | varchar(20)  | YES  |     | NULL     |       |
| salary  | decimal(7,2) | YES  |     | 20000.00 |       |
| email   | varchar(25)  | YES  | UNI | NULL     |       |
| age     | int          | YES  |     | NULL     |       |
| gender  | char(3)      | YES  |     | NULL     |       |
| city    | varchar(20)  | YES  |     | NULL     |       |
| doj     | date         | YES  |     | NULL     |       |
| dept_id | int          | YES  | MUL | NULL     |       |
+---------+--------------+------+-----+----------+-------+
9 rows in set (0.00 sec)

mysql> alter table employee
    -> modify column name varchar(20);
Query OK, 0 rows affected (0.07 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> desc employee;
+---------+--------------+------+-----+----------+-------+
| Field   | Type         | Null | Key | Default  | Extra |
+---------+--------------+------+-----+----------+-------+
| id      | int          | NO   | PRI | NULL     |       |
| name    | varchar(20)  | YES  |     | NULL     |       |
| salary  | decimal(7,2) | YES  |     | 20000.00 |       |
| email   | varchar(25)  | YES  | UNI | NULL     |       |
| age     | int          | YES  |     | NULL     |       |
| gender  | char(3)      | YES  |     | NULL     |       |
| city    | varchar(20)  | YES  |     | NULL     |       |
| doj     | date         | YES  |     | NULL     |       |
| dept_id | int          | YES  | MUL | NULL     |       |
+---------+--------------+------+-----+----------+-------+
9 rows in set (0.00 sec)

mysql> insert into employee
    -> (id, name,email,ahe,gender,city,doj,dept_id)
    -> values(102,"vinayak","manisha@gmail.com",22,'M',"PUNE","2025-11-1",1);
ERROR 1054 (42S22): Unknown column 'ahe' in 'field list'
mysql>  insert into employee
    -> (id,name,email,age,gender,city,doj,dept_id)
    -> values(102."manisha","manisha@gmail.com",21,'M',"pune","2025-11-1",1);
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '"manisha","manisha@gmail.com",21,'M',"pune","2025-11-1",1)' at line 3
mysql> insert into employee
    -> (id,name,email,age,gender,city,doj,dept_id)
    -> values(102,"manisha","manisha@gmail.com",21,'M',"pune","2025-11-1",1);
ERROR 1062 (23000): Duplicate entry 'manisha@gmail.com' for key 'employee.email'
mysql> insert into employee
    -> (id,name,email,age,gender,city,doj,dept_id)
    ->  values(103,"manisha","manisha@gmail.com",21,'M',"pune","2025-11-1",1);
ERROR 1062 (23000): Duplicate entry 'manisha@gmail.com' for key 'employee.email'
mysql>  insert into employee
    ->  (id,name,email,age,gender,city,doj,dept_id)
    ->  values(103,"manisha","manuu@google.com",21,'M',"pune","2025-11-1",1);
Query OK, 1 row affected (0.03 sec)

mysql> table employee;
+-----+---------+----------+-------------------+------+--------+------+------------+---------+
| id  | name    | salary   | email             | age  | gender | city | doj        | dept_id |
+-----+---------+----------+-------------------+------+--------+------+------------+---------+
| 101 | manuu   |  9000.00 | manisha@gmail.com |   21 | M      | pune | 2005-04-08 |       1 |
| 103 | manisha | 20000.00 | manuu@google.com  |   21 | M      | pune | 2025-11-01 |       1 |
+-----+---------+----------+-------------------+------+--------+------+------------+---------+
2 rows in set (0.00 sec)

mysql> table department;
+---------+-----------+----------+
| dept_id | dept_name | dept_loc |
+---------+-----------+----------+
|       1 | IT        | pune     |
+---------+-----------+----------+
1 row in set (0.00 sec)

mysql> insert into department
    -> values(2,"HR","Nagpure"),
    -> (3,"sales","mumbai");
Query OK, 2 rows affected (0.01 sec)
Records: 2  Duplicates: 0  Warnings: 0

mysql> table department;
+---------+-----------+----------+
| dept_id | dept_name | dept_loc |
+---------+-----------+----------+
|       1 | IT        | pune     |
|       2 | HR        | Nagpure  |
|       3 | sales     | mumbai   |
+---------+-----------+----------+
3 rows in set (0.00 sec)

mysql> alter table employee
    -> modify column id int auto_increment;
Query OK, 2 rows affected (0.25 sec)
Records: 2  Duplicates: 0  Warnings: 0

mysql> table employee;
+-----+---------+----------+-------------------+------+--------+------+------------+---------+
| id  | name    | salary   | email             | age  | gender | city | doj        | dept_id |
+-----+---------+----------+-------------------+------+--------+------+------------+---------+
| 101 | manuu   |  9000.00 | manisha@gmail.com |   21 | M      | pune | 2005-04-08 |       1 |
| 103 | manisha | 20000.00 | manuu@google.com  |   21 | M      | pune | 2025-11-01 |       1 |
+-----+---------+----------+-------------------+------+--------+------+------------+---------+
2 rows in set (0.00 sec)

mysql> insert into employee
    -> (name,salary,email,age,gender,city,doj,dept_id)
    -> values ("Bhavna",30000,sanjay@123.com,21,"M","pune","2023-10-10",2);
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '@123.com,21,"M","pune","2023-10-10",2)' at line 3
mysql>  insert into employee
    -> (name,salary,email,age,gender,city,doj,dept_id)
    -> values ("Bhavna",30000,"sanjay@amazon.com",21,"M","pune","2023-10-10",2);
Query OK, 1 row affected (0.04 sec)

mysql> table employee;
+-----+---------+----------+-------------------+------+--------+------+------------+---------+
| id  | name    | salary   | email             | age  | gender | city | doj        | dept_id |
+-----+---------+----------+-------------------+------+--------+------+------------+---------+
| 101 | manuu   |  9000.00 | manisha@gmail.com |   21 | M      | pune | 2005-04-08 |       1 |
| 103 | manisha | 20000.00 | manuu@google.com  |   21 | M      | pune | 2025-11-01 |       1 |
| 104 | Bhavna  | 30000.00 | sanjay@amazon.com |   21 | M      | pune | 2023-10-10 |       2 |
+-----+---------+----------+-------------------+------+--------+------+------------+---------+
3 rows in set (0.00 sec)

mysql> insert into employee
    ->  (name,salary,email,age,gender,city,doj,dept_id)
    ->  values ("sakshi",35000,"sakshi@amazon.com",21,"f","loha","2024-10-10",3),
    -> values ("vishal",33000,"vishal@amazon.com",22,"m","loha","2022-10-10",4),
    -> values ("nikita",32000,"nikita@amazon.com",23,"f","shelagaon","2021-10-10",5);
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'values ("vishal",33000,"vishal@amazon.com",22,"m","loha","2022-10-10",4),
values' at line 4
mysql> insert into employee
    -> (name,salary,email,age,gender,city,doj,dept_id)
    ->  values ("sakshi",35000,"sakshi@amazon.com",21,"f","loha","2024-10-10",3),
    -> ("vishal",33000,"vishal@amazon.com",22,"m","loha","2022-10-10",4),
    ->  ("nikita",32000,"nikita@amazon.com",23,"f","shelagaon","2021-10-10",5);
ERROR 1452 (23000): Cannot add or update a child row: a foreign key constraint fails (`may_apr_2026`.`employee`, CONSTRAINT `employee_ibfk_1` FOREIGN KEY (`dept_id`) REFERENCES `department` (`dept_id`))
mysql> show create table employee;
+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Table    | Create Table                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| employee | CREATE TABLE `employee` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(20) DEFAULT NULL,
  `salary` decimal(7,2) DEFAULT '20000.00',
  `email` varchar(25) DEFAULT NULL,
  `age` int DEFAULT NULL,
  `gender` char(3) DEFAULT NULL,
  `city` varchar(20) DEFAULT NULL,
  `doj` date DEFAULT NULL,
  `dept_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  KEY `dept_id` (`dept_id`),
  CONSTRAINT `employee_ibfk_1` FOREIGN KEY (`dept_id`) REFERENCES `department` (`dept_id`),
  CONSTRAINT `employee_chk_1` CHECK ((`age` >= 18))
) ENGINE=InnoDB AUTO_INCREMENT=108 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci |
+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
1 row in set (0.04 sec)

mysql> alter table employee
    -> drop forgign key employee_ibfk_1;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'key employee_ibfk_1' at line 2
mysql> show table;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '' at line 1
mysql> drop forgign key employee_ibfk_1;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'forgign key employee_ibfk_1' at line 1
mysql> ALTER TABLE employee
    -> DROP FOREIGN KEY employee_ibfk_1;
Query OK, 0 rows affected (0.04 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> insert into employee
    ->     ->  (name,salary,email,age,gender,city,doj,dept_id)
    ->     ->  values ("sakshi",35000,"sakshi@amazon.com",21,"f","loha","2024-10-10",3),
    ->     -> values ("vishal",33000,"vishal@amazon.com",22,"m","loha","2022-10-10",4),
    ->     -> values ("nikita",32000,"nikita@amazon.com",23,"f","shelagaon","2021-10-10",5);
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '->  (name,salary,email,age,gender,city,doj,dept_id)
    ->  values ("sakshi",350' at line 2
mysql> ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'values ("vishal",33000,"vishal@amazon.com",22,"m","loha","2022-10-10",4),
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'ERROR 1064 (42000): You have an error in your SQL syntax' at line 1
    '> values' at line 4
    -> mysql> insert into employee
    ->     -> (name,salary,email,age,gender,city,doj,dept_id)
    ->     ->  values ("sakshi",35000,"sakshi@amazon.com",21,"f","loha","2024-10-10",3),
    ->     -> ("vishal",33000,"vishal@amazon.com",22,"m","loha","2022-10-10",4),
    ->
    -> ("shubhi",35000,"shubhi@amazon.com",21,"f","shelagaon","2024-10-10",5),
    -> ("komal",34000,"komal@amazon.com",21,"f","shewala","2025-10-10",8);
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'the manual that corresponds to your MySQL server version for the right syntax to' at line 1
mysql> insert into employee
    -> (name,salary,email,age,gender,city,doj,dept_id)
    -> values ("sakshi",35000,"sakshi@amazon.com",21,"f","loha","2024-10-10",3),
    ->  ("vishal",33000,"vishal@amazon.com",22,"m","loha","2022-10-10",4),
    ->  ("shubhi",35000,"shubhi@amazon.com",21,"f","shelagaon","2024-10-10",5),
    ->  ("shubhi",35000,"shubhi@amazon.com",21,"f","shelagaon","2024-10-10",5);
ERROR 1062 (23000): Duplicate entry 'shubhi@amazon.com' for key 'employee.email'
mysql> insert into employee
    ->     -> (name,salary,email,age,gender,city,doj,dept_id)
    ->     -> values ("sakshi",35000,"sakshi@amazon.com",21,"f","loha","2024-10-10",3),
    ->     ->  ("vishal",33000,"vishal@amazon.com",22,"m","loha","2022-10-10",4),
    ->     ->  ("shubhi",35000,"shubhi@amazon.com",21,"f","shelagaon","2024-10-10",5);
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '-> (name,salary,email,age,gender,city,doj,dept_id)
    -> values ("sakshi",35000' at line 2
mysql>  insert into employee
    -> (name,salary,email,age,gender,city,doj,dept_id)
    ->  values ("sakshi",35000,"sakshi@amazon.com",21,"f","loha","2024-10-10",3),
    -> ("vishal",33000,"vishal@amazon.com",22,"m","loha","2022-10-10",4),
    -> ("shubhi",35000,"shubhi@amazon.com",21,"f","shelagaon","2024-10-10",5);
Query OK, 3 rows affected (0.02 sec)
Records: 3  Duplicates: 0  Warnings: 0

mysql> table employee;
+-----+---------+----------+-------------------+------+--------+-----------+------------+---------+
| id  | name    | salary   | email             | age  | gender | city      | doj        | dept_id |
+-----+---------+----------+-------------------+------+--------+-----------+------------+---------+
| 101 | manuu   |  9000.00 | manisha@gmail.com |   21 | M      | pune      | 2005-04-08 |       1 |
| 103 | manisha | 20000.00 | manuu@google.com  |   21 | M      | pune      | 2025-11-01 |       1 |
| 104 | Bhavna  | 30000.00 | sanjay@amazon.com |   21 | M      | pune      | 2023-10-10 |       2 |
| 112 | sakshi  | 35000.00 | sakshi@amazon.com |   21 | f      | loha      | 2024-10-10 |       3 |
| 113 | vishal  | 33000.00 | vishal@amazon.com |   22 | m      | loha      | 2022-10-10 |       4 |
| 114 | shubhi  | 35000.00 | shubhi@amazon.com |   21 | f      | shelagaon | 2024-10-10 |       5 |
+-----+---------+----------+-------------------+------+--------+-----------+------------+---------+
6 rows in set (0.00 sec)

mysql> table department;
+---------+-----------+----------+
| dept_id | dept_name | dept_loc |
+---------+-----------+----------+
|       1 | IT        | pune     |
|       2 | HR        | Nagpure  |
|       3 | sales     | mumbai   |
+---------+-----------+----------+
3 rows in set (0.00 sec)

mysql> update employee
    -> set salary=36000
    -> where id = 103;
Query OK, 1 row affected (0.02 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> table employee;
+-----+---------+----------+-------------------+------+--------+-----------+------------+---------+
| id  | name    | salary   | email             | age  | gender | city      | doj        | dept_id |
+-----+---------+----------+-------------------+------+--------+-----------+------------+---------+
| 101 | manuu   |  9000.00 | manisha@gmail.com |   21 | M      | pune      | 2005-04-08 |       1 |
| 103 | manisha | 36000.00 | manuu@google.com  |   21 | M      | pune      | 2025-11-01 |       1 |
| 104 | Bhavna  | 30000.00 | sanjay@amazon.com |   21 | M      | pune      | 2023-10-10 |       2 |
| 112 | sakshi  | 35000.00 | sakshi@amazon.com |   21 | f      | loha      | 2024-10-10 |       3 |
| 113 | vishal  | 33000.00 | vishal@amazon.com |   22 | m      | loha      | 2022-10-10 |       4 |
| 114 | shubhi  | 35000.00 | shubhi@amazon.com |   21 | f      | shelagaon | 2024-10-10 |       5 |
+-----+---------+----------+-------------------+------+--------+-----------+------------+---------+
6 rows in set (0.00 sec)

mysql> update employee
    -> set salary =salary+20000
    -> where age > 22;
Query OK, 0 rows affected (0.05 sec)
Rows matched: 0  Changed: 0  Warnings: 0

mysql> table employee;
+-----+---------+----------+-------------------+------+--------+-----------+------------+---------+
| id  | name    | salary   | email             | age  | gender | city      | doj        | dept_id |
+-----+---------+----------+-------------------+------+--------+-----------+------------+---------+
| 101 | manuu   |  9000.00 | manisha@gmail.com |   21 | M      | pune      | 2005-04-08 |       1 |
| 103 | manisha | 36000.00 | manuu@google.com  |   21 | M      | pune      | 2025-11-01 |       1 |
| 104 | Bhavna  | 30000.00 | sanjay@amazon.com |   21 | M      | pune      | 2023-10-10 |       2 |
| 112 | sakshi  | 35000.00 | sakshi@amazon.com |   21 | f      | loha      | 2024-10-10 |       3 |
| 113 | vishal  | 33000.00 | vishal@amazon.com |   22 | m      | loha      | 2022-10-10 |       4 |
| 114 | shubhi  | 35000.00 | shubhi@amazon.com |   21 | f      | shelagaon | 2024-10-10 |       5 |
+-----+---------+----------+-------------------+------+--------+-----------+------------+---------+
6 rows in set (0.00 sec)

mysql> update employee
    -> set salary=salary+3000
    -> where gender="f" and age >21;
Query OK, 0 rows affected (0.00 sec)
Rows matched: 0  Changed: 0  Warnings: 0