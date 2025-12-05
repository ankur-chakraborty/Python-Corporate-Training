CREATE DATABASE IF NOT EXISTS employee_app;
USE employee_app;
 
DROP TABLE IF EXISTS employees;
 
CREATE TABLE employees (
  emp_id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  dept VARCHAR(100),
  role VARCHAR(100),
  salary DECIMAL(10,2) NOT NULL DEFAULT 0.00,
  email VARCHAR(120) UNIQUE,
  phone VARCHAR(20),
  hired_on DATE NOT NULL DEFAULT (CURRENT_DATE)
);
 
INSERT INTO employees (name, dept, role, salary, email, phone, hired_on) VALUES
('Aisha Khan', 'HR', 'Generalist', 45000, 'aisha@example.com', '9999900001', '2024-12-01'),
('Rahul Sharma', 'Sales', 'Executive', 52000, 'rahul@example.com', '9999900002', '2025-01-12'),
('Meera Iyer', 'Engineering', 'Developer', 80000, 'meera@example.com', '9999900003', '2025-02-05');