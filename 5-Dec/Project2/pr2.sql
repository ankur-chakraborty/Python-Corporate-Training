CREATE DATABASE IF NOT EXISTS retail_app;
USE retail_app;
 
DROP TABLE IF EXISTS orders;
 
CREATE TABLE orders (
  order_id INT PRIMARY KEY,
  order_date DATE NOT NULL,
  customer_id INT NOT NULL,
  customer_name VARCHAR(120) NOT NULL,
  sku VARCHAR(50) NOT NULL,
  quantity INT NOT NULL,
  unit_price DECIMAL(10,2) NOT NULL
);
 
INSERT INTO orders (order_id, order_date, customer_id, customer_name, sku, quantity, unit_price) VALUES
(1001, '2025-11-28', 1, 'Rahul Sharma', 'SKU-101', 2, 499.00),
(1002, '2025-11-29', 2, 'Aisha Khan',   'SKU-102', 1, 1299.00),
(1003, '2025-12-01', 2, 'Aisha Khan',   'SKU-101', 3, 459.00),
(1004, '2025-12-03', 3, 'Ravi Kumar',   'SKU-103', 5, 199.00);