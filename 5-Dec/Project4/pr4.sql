CREATE DATABASE IF NOT EXISTS billing_app;
USE billing_app;
 
DROP TABLE IF EXISTS invoice_items;
DROP TABLE IF EXISTS invoices;
 
CREATE TABLE invoices (
  invoice_id INT AUTO_INCREMENT PRIMARY KEY,
  invoice_no VARCHAR(30) UNIQUE,
  created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  customer_name VARCHAR(150) NOT NULL,
  customer_phone VARCHAR(20),
  subtotal DECIMAL(12,2) NOT NULL,
  discount_total DECIMAL(12,2) NOT NULL,
  tax_total DECIMAL(12,2) NOT NULL,
  grand_total DECIMAL(12,2) NOT NULL,
  notes VARCHAR(255)
);
 
CREATE TABLE invoice_items (
  item_id INT AUTO_INCREMENT PRIMARY KEY,
  invoice_id INT NOT NULL,
  sku VARCHAR(30) NOT NULL,
  name VARCHAR(150) NOT NULL,
  qty INT NOT NULL,
  unit_price DECIMAL(12,2) NOT NULL,
  discount_pct DECIMAL(5,2) NOT NULL DEFAULT 0,
  tax_pct DECIMAL(5,2) NOT NULL DEFAULT 0,
  line_subtotal DECIMAL(12,2) NOT NULL,
  line_discount DECIMAL(12,2) NOT NULL,
  line_tax DECIMAL(12,2) NOT NULL,
  line_total DECIMAL(12,2) NOT NULL,
  CONSTRAINT fk_item_invoice FOREIGN KEY (invoice_id) REFERENCES invoices(invoice_id),
  INDEX idx_invoice (invoice_id)
);