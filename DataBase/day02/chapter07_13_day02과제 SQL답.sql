--USE mysql;
--과제2 데이터베이스와 테이블 생성

--1) 데이터 베이스 생성( fishbread_db)
--CREATE DATABASE fishbread_db;
--USE fishbread_db;

--2) users 테이블 생성
--CREATE TABLE users (
--user_id INT AUTO-INCREMENT PRIMARY KEY,
--name VARCHAR(255) NOT NULL,
--age INT NOT NULL,
--email VARCHAR(100) UNIQUE,
--is_business BOOL
--);

--3) orders 테이블 생성
--CREATE TABLE orders (
--    -> order_id INT AUTO_INCREMENT PRIMARY KEY,
--    -> user_id INT,
--    -> order_date DATE,
--    -> amount DECIMAL(10, 2),
--    -> FOREIGN KEY(user_id) REFERENCES users(user_id)
--    -> );

--4) inventory 테이블 생성
--CREATE TABLE inventory (
--    -> item_id INT AUTO_INCREMENT PRIMARY KEY,
--    -> item_name VARCHAR(255) NOT NULL,
--    -> quantity INT NOT NULL
--    -> );


--5) sales 테이블 생성
--CREATE TABLE sales (
--    -> sale_id INT AUTO_INCREMENT PRIMARY KEY,
--    -> order_id INT,
--    -> Item_id INT,
--    -> quantity_sold INT NOT NULL,
--    -> CONSTRAINT oder_id FOREIGN KEY (order_id) REFERENCES orders(order_id),                 
--    -> CONSTRAINT item_id FOREIGN KEY (item_id) REFERENCES inventory(item_id)                 
--    -> );

--6) daily_sales 테이블 생성
--CREATE TABLE daily_sales (
--    -> daily_sales_id INT,
--    -> sale_id INT,
--    -> daily_sales DATE PRIMARY KEY,
--    -> total_sales DECIMAL(10, 2) NOT NULL,
--    -> FOREIGN KEY(sale_id) REFERENCES sales(sale_id)                 
--    -> );
