CREATE DATABASE college_db;
USE college_db;

Create table students(
	student_id INT auto_increment PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    age INT,
    city VARCHAR(50)
);



INSERT INTO students(first_name, last_name, email, age, city) 
VALUES 
('Aisha', 'Kapoor', 'aisha@exam.com', 20, 'Mumbai'),
('Ankur', 'KChakraborty', 'ankur@exam.com', 22, 'Kolkata'),
('Dipsu', 'Das', 'Dipsu@exam.com', 25, 'Delhi'),
('Messi', 'Lionel', 'Messi@exam.com', 38, 'Argentina');

select * from students;



select * from students where city='Delhi';

select * from students order by age desc;

SET SQL_SAFE_UPDATES = 0; #Done to prevent error 1175

update students set city= 'Bangalore'
where student_id=2;

update students
set age=24
where email='Messi@exam.com';


Delete from students
where city = 'Mumbai';

drop table students;
drop database college_db;



