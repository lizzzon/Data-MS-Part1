SELECT * FROM users
WHERE POSITION('@mail.ru' in email) > 0;

SELECT POSITION('@gmail.com' in email) FROM users;

SELECT product_cost FROM products
ORDER BY product_cost DESC;

SELECT user_id, last_name, first_name, address FROM users
WHERE phone LIKE '_375%';

SELECT AVG(product_cost) AS averege_product_cost FROM products;

SELECT AVG(product_cost) FROM products
WHERE product_name = 'ASUS';

SELECT SUM(product_amount * product_cost) FROM products;

UPDATE users SET user_password = '374type73'
             WHERE user_password = '758305';

UPDATE loans SET loan_amount = loan_amount + 1
WHERE client_id = 1 AND product_id = 1
RETURN loan_amount;

UPDATE products SET product_name = product_name + 1 FROM product_types
                WHERE product_types.product_type_name = 'Computer'
                AND products.id = product_types.id;

ALTER TABLE companies ADD COLUMN address VARCHAR(32);

ALTER TABLE companies DROP COLUMN address RESTRICT;

ALTER TABLE clients RENAME COLUMN phone TO telephone;

ALTER TABLE logs
    ALTER COLUMN time_stamp DROP DEFAULT,
    ALTER COLUMN time_stamp TYPE timestamp with time zone
    USING
        timestamp with time zone 'epoch' + time_stamp * interval '1 second',
    ALTER COLUMN time_stamp SET DEFAULT now();

ALTER TABLE companies ALTER COLUMN short_name DROP NOT NULL;