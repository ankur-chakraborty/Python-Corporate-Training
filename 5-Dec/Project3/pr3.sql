CREATE DATABASE IF NOT EXISTS library_app;
USE library_app;
 
DROP TABLE IF EXISTS borrows;
DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS members;
 
CREATE TABLE books (
  book_id INT AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(200) NOT NULL,
  author VARCHAR(150) NOT NULL,
  isbn VARCHAR(20) UNIQUE,
  copies_total INT NOT NULL DEFAULT 1,
  copies_available INT NOT NULL DEFAULT 1
);
 
CREATE TABLE members (
  member_id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(150) NOT NULL,
  email VARCHAR(150) UNIQUE,
  phone VARCHAR(20),
  joined_on DATE NOT NULL DEFAULT (CURRENT_DATE)
);
 
CREATE TABLE borrows (
  borrow_id INT AUTO_INCREMENT PRIMARY KEY,
  member_id INT NOT NULL,
  book_id INT NOT NULL,
  borrow_date DATE NOT NULL DEFAULT (CURRENT_DATE),
  due_date DATE NOT NULL,
  return_date DATE NULL,
  status ENUM('Borrowed','Returned') NOT NULL DEFAULT 'Borrowed',
  CONSTRAINT fk_b_member FOREIGN KEY (member_id) REFERENCES members(member_id),
  CONSTRAINT fk_b_book FOREIGN KEY (book_id) REFERENCES books(book_id),
  INDEX idx_borrow_member (member_id),
  INDEX idx_borrow_book (book_id)
);
 
INSERT INTO books (title, author, isbn, copies_total, copies_available) VALUES
('Clean Code', 'Robert C. Martin', '9780132350884', 3, 3),
('The Pragmatic Programmer', 'Andrew Hunt', '9780201616224', 2, 2),
('Introduction to Algorithms', 'Thomas H. Cormen', '9780262033848', 1, 1);
 
INSERT INTO members (name, email, phone, joined_on) VALUES
('Rahul Sharma', 'rahul@libmail.com', '9000000001', '2025-01-10'),
('Aisha Khan', 'aisha@libmail.com', '9000000002', '2024-12-05');