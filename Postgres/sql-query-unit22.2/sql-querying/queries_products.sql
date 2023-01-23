-- Comments in SQL Start with dash-dash --
-- Products Querying
-- Add a product to the table with the name of “chair”, price of 44.00, and can_be_returned of false.
INSERT INTO products(name,price,can_be_returned) 
VALUES ('chair',44.00,false);

-- Add a product to the table with the name of “stool”, price of 25.99, and can_be_returned of true.
INSERT INTO products(name,price,can_be_returned) 
VALUES ('stool',25.99,true);

-- Add a product to the table with the name of “table”, price of 124.00, and can_be_returned of false.
INSERT INTO products(name,price,can_be_returned) 
VALUES ('table',124.00,false);

-- Display all of the rows and columns in the table.
SELECT * FROM products;

-- Display all of the names of the products.
SELECT name FROM products;

-- Display all of the names and prices of the products.
SELECT name, price FROM products;

-- Add a new product - make up whatever you would like!
INSERT INTO products(name,price,can_be_returned) 
VALUES ('barstool',100.00,true);

-- Display only the products that can_be_returned.
SELECT * FROM products WHERE can_be_returned = true;

-- Display only the products that have a price less than 44.00.
SELECT * FROM products WHERE price < 44.00;

-- Display only the products that have a price in between 22.50 and 99.99.
SELECT * FROM products WHERE price BETWEEN 22.50 AND 99.99;

-- There’s a sale going on: Everything is $20 off! Update the database accordingly.
UPDATE products SET price = price - 20;

-- Because of the sale, everything that costs less than $25 has sold out. Remove all products whose price meets this criteria.
DELETE FROM products WHERE price < 25;

-- And now the sale is over. For the remaining products, increase their price by $20.
UPDATE products SET price = price + 20;

-- There is a new company policy: everything is returnable. Update the database accordingly.
UPDATE products SET can_be_returned = true;
