SELECT product_name , supplier_id , unit_price,
       unit_price * 0.14 / (2.74 + 52.36)
FROM   products

SELECT Product_name , unit_price , Discount
       unit_price - Discount
FROM   products

/*
In Oracle The plus (+) and minus (-) operators can be used to perform arithmetic operations on Date values. These operators will allow you to add or subtract days.
*/

SELECT order_id , customer_name , order_date, order_date + 1
FROM orders

/*
In Oracle A NULL value is a value that indicates an empty field in a table. This value does not equal zero (0), nor does it equal space (‘ ‘); When a certain calculation is carried out on a column that contains NULL values, any calculation performed on the NULL value returns NULL.
*/

SELECT product_name, unit_price, discount,
       discount + 1
FROM products 
 
SELECT product_name, unit_price, discount ,
       discount * unit_price
FROM products

SELECT product_name, unit_price, unit_price  + 500  AS "NEW_UNIT_PRICE"
FROM products

SELECT DISTINCT city , country
FROM            customers

SELECT customer_id, last_name, birthdate 
FROM customers
WHERE birthdate > '13-JAN-1982'

/*
In Oracle the string value must be enclosed within single quotes (‘string value’).
*/

SELECT product_id, product_name  
FROM products
WHERE  product_name = 'Tea'
-- (valid comparison)
 
SELECT customer_id, first_name, last_name
FROM customers
WHERE first_name = 'John'
-- (valid comparison)

SELECT product_id, product_name, unit_price
FROM products
WHERE  unit_price IN (50, 80, 90)

SELECT customer_id, first_name, last_name, birthdate, city
FROM customers
WHERE  city NOT IN ('London', 'Paris', 'Berlin')

SELECT product_id, product_name, unit_price
FROM products
WHERE  unit_price = 50 
OR     unit_price = 80
OR     unit_price = 90

SELECT customer_id, first_name, last_name, birthdate
FROM customers
 WHERE birthdate IN ('01-JAN-1990', '07-SEP-1982')

SELECT customer_id, first_name, last_name, birthdate
FROM customers
WHERE birthdate = '01-JAN-1990'
OR    birthdate = '07-SEP-1982'


SELECT product_id, product_name, unit_price
FROM products
WHERE unit_price BETWEEN 50 AND 80

SELECT product_id, product_name, unit_price
FROM products
WHERE  unit_price NOT BETWEEN 50 AND 80

SELECT product_name
FROM products
WHERE  product_name BETWEEN 'A' AND 'G'

SELECT customer_id, first_name, birthdate
FROM customers
WHERE birthdate BETWEEN '01-JAN-1990' AND '01-JAN-2000'

SELECT product_name
FROM products
WHERE  product_name LIKE '_a%'

SELECT product_id, product_name, unit_price, discount
FROM products
WHERE  discount IS NULL 