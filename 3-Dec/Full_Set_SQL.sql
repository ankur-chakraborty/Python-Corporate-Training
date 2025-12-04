CREATE DATABASE retail_db;
USE retail_db;

CREATE TABLE customers (
customer_id INT PRIMARY KEY,
customer_name VARCHAR(50),
email VARCHAR(80),
city VARCHAR(50)
);

CREATE TABLE orders (
order_id INT PRIMARY KEY,
order_date DATE,
customer_id INT NULL,
total_amount DECIMAL(10,2),
product_id INT NULL
);



CREATE TABLE products (
product_id INT PRIMARY KEY,
product_name VARCHAR(100),
category VARCHAR(50),
price DECIMAL(10,2)
);



INSERT INTO customers VALUES
(1, 'Aisha Khan', 'aisha@xyz.com', 'Mumbai'),
(2, 'Rahul Sharma', 'rahul@xyz.com', 'Delhi'),
(3, 'John Daniel', 'john@xyz.com', 'Bangalore'),
(4, 'Meera Iyer', 'meera@xyz.com', 'Chennai'),
(5, 'Sanjay Patel', 'sanjay@xyz.com', 'Hyderabad');




INSERT INTO products VALUES
(101, 'Laptop HP 15', 'Electronics', 52000),
(102, 'Samsung Phone A54', 'Electronics', 28000),
(103, 'Jeans Blue Fit', 'Fashion', 1500),
(104, 'T-Shirt Classic', 'Fashion', 700),
(105, 'Wireless Mouse', 'Accessories', 900),
(106, 'Rice 5KG Bag', 'Groceries', 320),
(107, 'Olive Oil 1L', 'Groceries', 540),
(108, 'Printer Canon G2012', 'Electronics', 12500);



INSERT INTO orders VALUES
(1001, '2024-01-05', 1, 52000, 101),
(1002, '2024-01-06', 2, 28000, 102),
(1003, '2024-01-07', 3, 1500, 103),
(1004, '2024-01-07', 1, 700, 104),
(1005, '2024-01-08', 2, 900, 105),
(1006, '2024-01-08', NULL, 320, 106), -- customer unknown
(1007, '2024-01-09', 1, 540, NULL), -- product unknown
(1008, '2024-01-10', 3, 12500, 108),
(1009, '2024-01-10', 4, 320, 106),
(1010, '2024-01-11', NULL, 700, 104), -- customer null
(1011, '2024-01-12', 2, 540, 107); -- product exists but never order



#Q1
SELECT 
    o.order_id,
    o.order_date,
    o.total_amount,
    c.customer_name,
    c.email
FROM orders AS o
INNER JOIN customers AS c
    ON o.customer_id = c.customer_id;
    
    
    

#Q2
select o.order_id, p.product_name, p.category, p.price
from products as p
inner join orders as o
on p.product_id=o.product_id;


#Q3

SELECT 
    o.order_id,
    o.order_date,
    c.customer_name,
    p.product_name
FROM orders AS o
INNER JOIN customers AS c
    ON o.customer_id = c.customer_id
INNER JOIN products AS p
    ON o.product_id = p.product_id;
    
    
#Q4

SELECT 
    c.customer_name,
    o.total_amount
FROM orders AS o
INNER JOIN customers AS c
    ON o.customer_id = c.customer_id;



#Q5


SELECT DISTINCT 
    p.product_name,
    p.category,
    p.price
FROM orders AS o
INNER JOIN products AS p
    ON o.product_id = p.product_id
WHERE p.category = 'Electronics';




#Q6


SELECT DISTINCT 
    c.customer_name,
    c.email
FROM orders AS o
INNER JOIN customers AS c
    ON o.customer_id = c.customer_id
INNER JOIN products AS p
    ON o.product_id = p.product_id
WHERE p.category = 'Fashion';




#Q7


SELECT 
    o.order_id,
    o.order_date,
    o.total_amount,
    c.customer_name,
    p.product_name,
    p.category
FROM orders AS o
INNER JOIN customers AS c
    ON o.customer_id = c.customer_id
INNER JOIN products AS p
    ON o.product_id = p.product_id
WHERE o.total_amount > 1000;


#Q8


SELECT DISTINCT 
    c.customer_name,
    c.city
FROM orders AS o
INNER JOIN customers AS c
    ON o.customer_id = c.customer_id
WHERE c.city = 'Mumbai';



#Q9

SELECT 
    c.customer_name,
    COUNT(o.order_id) AS order_count
FROM customers AS c
INNER JOIN orders AS o
    ON c.customer_id = o.customer_id
GROUP BY c.customer_name;



#Q10


SELECT 
    c.customer_name,
    SUM(o.total_amount) AS total_spent
FROM customers AS c
INNER JOIN orders AS o
    ON c.customer_id = o.customer_id
GROUP BY c.customer_name;



#Q11


SELECT 
    o.order_id,
    o.order_date,
    o.total_amount,
    c.customer_name,
    c.email
FROM orders AS o
LEFT JOIN customers AS c
    ON o.customer_id = c.customer_id;



#Q12


SELECT *
FROM orders
WHERE customer_id IS NULL;




#Q13


SELECT 
    o.order_id,
    o.order_date,
    o.total_amount,
    c.city
FROM orders AS o
LEFT JOIN customers AS c
    ON o.customer_id = c.customer_id;



#Q14

SELECT 
    c.customer_name,
    COUNT(o.order_id) AS order_count
FROM customers AS c
LEFT JOIN orders AS o
    ON c.customer_id = o.customer_id
GROUP BY c.customer_name;




#q15


SELECT 
    c.customer_name
FROM customers AS c
LEFT JOIN orders AS o
    ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL;




#Q16


SELECT 
    o.order_id,
    o.order_date,
    COALESCE(c.customer_name, 'Guest Checkout') AS customer_name,
    o.total_amount
FROM orders AS o
LEFT JOIN customers AS c
    ON o.customer_id = c.customer_id;






#Q17


SELECT *
FROM orders
WHERE product_id IS NULL;





#Q18

SELECT 
    o.order_id,
    o.order_date,
    o.total_amount,
    c.city
FROM orders AS o
LEFT JOIN customers AS c
    ON o.customer_id = c.customer_id
WHERE c.city = 'Delhi' OR c.city IS NULL;





#Q19

SELECT COUNT(*) AS total_orders
FROM orders;




#Q20

SELECT 
    ROUND(
        (SUM(CASE WHEN customer_id IS NULL THEN 1 ELSE 0 END) * 100.0) / COUNT(*),
        2
    ) AS missing_customer_percentage
FROM orders;




#Q21

SELECT
    p.product_id,
    p.product_name,
    p.category,
    p.price,
    o.order_id,
    o.order_date,
    o.customer_id,
    o.total_amount
FROM products AS p
LEFT JOIN orders AS o
    ON p.product_id = o.product_id
ORDER BY p.product_id, o.order_id;





#Q22

SELECT
    p.product_id,
    p.product_name,
    p.category,
    p.price
FROM products AS p
LEFT JOIN orders AS o
    ON p.product_id = o.product_id
WHERE o.order_id IS NULL;



#Q23

SELECT
    p.product_name,
    COUNT(o.order_id) AS times_ordered
FROM products AS p
LEFT JOIN orders AS o
    ON p.product_id = o.product_id
WHERE p.category = 'Electronics'
GROUP BY p.product_name;



#Q24

SELECT
    p.product_name,
    MIN(o.order_date) AS first_order_date
FROM products AS p
LEFT JOIN orders AS o
    ON p.product_id = o.product_id
WHERE p.category = 'Groceries'
GROUP BY p.product_name;





#Q25

SELECT
    p.product_name,
    COALESCE(SUM(o.total_amount), 0) AS total_sales
FROM products AS p
LEFT JOIN orders AS o
    ON p.product_id = o.product_id
GROUP BY p.product_name
ORDER BY total_sales DESC;




#Q26

SELECT
    p.category,
    COUNT(DISTINCT o.product_id) AS ordered_product_count
FROM products AS p
LEFT JOIN orders AS o
    ON p.product_id = o.product_id
GROUP BY p.category
ORDER BY p.category;





#Q27

SELECT DISTINCT
    p.product_id,
    p.product_name,
    p.category
FROM orders AS o
INNER JOIN customers AS c
    ON o.customer_id = c.customer_id
INNER JOIN products AS p
    ON o.product_id = p.product_id
WHERE c.city = 'Bangalore';




#Q28

SELECT
    p.product_id,
    p.product_name,
    p.category
FROM products AS p
LEFT JOIN orders AS o
    ON p.product_id = o.product_id
WHERE o.product_id IS NULL;





#Q29

SELECT
    p.product_name,
    COUNT(o.order_id) AS order_count
FROM products AS p
LEFT JOIN orders AS o
    ON p.product_id = o.product_id
GROUP BY p.product_name
ORDER BY order_count DESC, p.product_name;



#Q30

SELECT DISTINCT
    p.product_id,
    p.product_name,
    p.category
FROM products AS p
INNER JOIN orders AS o
    ON p.product_id = o.product_id
WHERE o.customer_id IS NULL;
