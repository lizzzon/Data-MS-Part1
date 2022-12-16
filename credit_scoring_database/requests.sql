SELECT * FROM users
WHERE POSITION('@mail.ru' in email) > 0;

SELECT POSITION('@gmail.com' in email) FROM users;

SELECT product_cost FROM products
ORDER BY product_cost DESC;

SELECT user_id, last_name, first_name, address FROM clients
WHERE phone LIKE '_375%';

SELECT AVG(product_cost) AS averege_product_cost FROM products;

SELECT AVG(product_cost) FROM products
WHERE product_name = 'ASUS zenbook';

SELECT SUM(product_amount * product_cost) FROM products;

UPDATE users SET user_password = '374type73'
             WHERE user_password = '758305';

UPDATE loans SET order_amount = order_amount + 1
WHERE client_id = 1 AND product_id = 1;

ALTER TABLE companies ADD COLUMN address VARCHAR(32);

ALTER TABLE companies DROP COLUMN address RESTRICT;

ALTER TABLE clients RENAME COLUMN phone TO telephone;

ALTER TABLE companies ALTER COLUMN short_name DROP NOT NULL;