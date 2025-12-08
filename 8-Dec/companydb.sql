create database company;
use company;


create table employees(
	id INT PRIMARY KEY auto_increment,
    name varchar(50),
    role varchar(50),
    salary INT
);


INSERT INTO employees (name, role, salary) VALUES 
('Ankur',22,50000),
('Dipsu',23,54000);