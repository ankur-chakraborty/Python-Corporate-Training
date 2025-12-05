CREATE DATABASE  retail_app;
USE retail_app;
 
 
CREATE TABLE customer (
  customer_id   INT PRIMARY KEY,
  name          VARCHAR(100) NOT NULL,
  email         VARCHAR(150) UNIQUE,
  city          VARCHAR(100),
  signup_date   DATE
);
 
 
CREATE TABLE product (
  product_id    INT PRIMARY KEY,
  product_name  VARCHAR(120) NOT NULL,
  category      VARCHAR(80) NOT NULL,
  unit_price    DECIMAL(10,2) NOT NULL
);
 
CREATE TABLE r_orders (
  order_id      INT PRIMARY KEY,
  customer_id   INT,
  product_id    INT,
  quantity      INT NOT NULL,
  unit_price    DECIMAL(10,2) NOT NULL, 
  order_date    DATE,
  FOREIGN KEY (customer_id) REFERENCES customer(customer_id),
  FOREIGN KEY (product_id)  REFERENCES product(product_id)
);
 
INSERT INTO customer (customer_id, name, email, city, signup_date) VALUES
(1, 'Asha',   'asha@example.com',   'Kolkata',  '2024-12-10'),
(2, 'Vikram', 'vikram@example.com', 'Delhi',    '2024-12-12'),
(3, 'Neha',   'neha@example.com',   'Mumbai',   '2024-12-15'),
(4, 'Rohit',  'rohit@example.com',  'Pune',     '2024-12-18'),
(5, 'Kabir',  'kabir@example.com',  'Kolkata',  '2024-12-20'),
(6, 'Ananya', 'ananya@example.com', 'Chennai',  '2024-12-22'),
(7, 'Leena',  'leena@example.com',  'Bengaluru','2024-12-24'),
(8, 'Arjun',  'arjun@example.com',  'Hyderabad','2024-12-26'),
(9, 'Priya',  'priya@example.com',  'Jaipur',   '2024-12-28'),
(10,'Dev',    'dev@example.com',    'Lucknow',  '2024-12-30');
 
INSERT INTO product (product_id, product_name, category, unit_price) VALUES
(101, 'Phone',       'Electronics', 15000.00),
(102, 'Headphones',  'Electronics',  2500.00),
(103, 'Case',        'Accessories',   500.00),
(104, 'T-Shirt',     'Clothing',      800.00),
(105, 'Jeans',       'Clothing',     1500.00),
(106, 'Rice',        'Grocery',        60.00),
(107, 'Milk',        'Grocery',        50.00),
(108, 'Blender',     'Home',         2200.00);
 
INSERT INTO r_orders (order_id, customer_id, product_id, quantity, unit_price, order_date) VALUES
(1001, 1, 101, 1, 15000.00, '2025-01-05'),
(1002, 1, 103, 2,   500.00, '2025-01-15'),
(1003, 1, 102, 1,  2500.00, '2025-02-20'), 
(1004, 2, 106, 5,    60.00, '2025-02-03'),
(1005, 3, 105, 2,  1500.00, '2025-02-10'),
(1006, 3, 107,10,    50.00, '2025-03-02'),
(1007, 4, 108, 1,  2200.00, '2025-03-15'),
(1008, 5, 104, 3,   800.00, '2025-04-01'),
(1009, 7, 106,20,    60.00, '2025-04-18'),
(1010, 7, 101, 1, 15000.00, '2025-05-02');
 
select customer_id, COUNT(*) AS total_orders
from r_orders
group by customer_id
having count(*)>2;
 
select * from product p
left join r_orders o 
on p.product_id = o.product_id
where o.product_id is null;
 
select customer_id, sum(unit_price*quantity) as total_spent
from r_orders
group by customer_id;
 
 
select o.order_id, p.product_id, p.product_name
from r_orders o
right join product p 
on o.product_id = p.product_id;
 
select o.customer_id
from r_orders o
join product p 
on o.product_id = p.product_id
group by o.customer_id
having count(distinct p.category)>1;
 
 
SELECT
  order_id,
  SUM(unit_price * quantity) AS order_total
FROM r_orders
GROUP BY order_id
ORDER BY order_total DESC
LIMIT 3;
 
 
SELECT *
FROM r_orders
WHERE customer_id IS NULL OR product_id IS NULL;
 
 
SELECT
  o.customer_id,
  EXTRACT(MONTH FROM order_date) as month,
  SUM(o.unit_price * o.quantity) AS total_amount
FROM r_orders o
GROUP BY o.customer_id, EXTRACT(MONTH FROM order_date)
order by customer_id, month;
 
select c.customer_id, p.product_id
from customer c
cross join product p;