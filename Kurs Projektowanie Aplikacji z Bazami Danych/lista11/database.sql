CREATE DATABASE ecommerce;
USE ecommerce;

CREATE TABLE products (
  id integer PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  category VARCHAR(50),
  price DECIMAL(10,2),
  availability ENUM('available', 'unavailable')
);


CREATE TABLE specimens (
    id integer PRIMARY KEY AUTO_INCREMENT,
    productId integer,
    FOREIGN KEY (productId) REFERENCES products(id),
    quantity integer,
    orderId integer,
    FOREIGN KEY (orderId) REFERENCES orders(id) ON DELETE CASCADE
);

CREATE TABLE orders(
    id integer PRIMARY KEY AUTO_INCREMENT,
    customerId integer,
    FOREIGN KEY (customerId) REFERENCES customers(id) ON DELETE CASCADE,
    total DECIMAL(10,2),
    purchase_status ENUM('fulfilled', 'waiting'),
    added TIMESTAMP NOT NULL DEFAULT NOW()
);


CREATE TABLE customers (
    id integer PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(20),
    surname VARCHAR(30),
    email VARCHAR(20)
);


-- Add customers
INSERT INTO customers (name, surname, email) VALUES
  ('John', 'Doe', 'john.doe@email.com'),
  ('Adam', 'Smith', 'jane.smith@email.com');

-- Add orders
INSERT INTO orders (customerId, total, purchase_status, added) VALUES
  (1, 150.00, 'waiting', NOW()),
  (2, 200.50, 'fulfilled', NOW()),
  (1, 10.20, 'fulfilled', NOW());
    

-- Add products
INSERT INTO products (name, description, category, price, availability) VALUES
  ('Laptop', 'Powerful laptop for multitasking', 'Electronics', 899.99, 'available'),
  ('Smartphone', 'Latest model with great camera', 'Electronics', 599.99, 'available'),
  ('Coffee Maker', 'Automatic coffee maker for home use', 'Appliances', 49.99, 'available');


INSERT INTO specimens (productId, quantity, orderId) VALUES 
(1, 2, 1);
