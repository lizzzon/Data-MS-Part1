--Request with multiple conditions
SELECT * FROM users
WHERE email = 'mail.ru' AND user_role = 'staff'
ORDER BY username ASC;

--Query with nested construct
SELECT phone,
    (SELECT username FROM users
     WHERE users.id = clients.id) AS first_name
FROM clients;

--INNER JOIN
SELECT users.username
FROM users
JOIN clients ON users.id = clients.user_id;

--OUTER JOIN
--LEFT
SELECT products.product_name, product_types.product_type_name
FROM products
LEFT JOIN product_types ON products.id = product_types.products_id;

--RIGHT
SELECT products.product_name, product_types.product_type_name
FROM product_types
RIGHT JOIN products ON products.id = product_types.products_id;

--FULL
SELECT clients.first_name, clients.last_name
FROM clients
FULL JOIN loans ON clients.id = loans.client_id;

--CROSS JOIN
SELECT * FROM users CROSS JOIN staff;

--SELF JOIN
SELECT c1.phone, c1.country_id, c2.phone
FROM clients c1
INNER JOIN clients c2 ON c1.id <> c2.id AND c1.country_id = c2.country_id;

--GROUP BY
SELECT product_amount, COUNT(*)
FROM products
GROUP BY product_amount
ORDER BY product_amount ASC;

--HAVING
SELECT clients.user_id, SUM(loans.order_amount)
FROM loans
LEFT JOIN clients ON clients.id = loans.client_id
GROUP BY clients.user_id
HAVING SUM(loans.order_amount) > 0
ORDER BY clients.user_id;

--UNION
SELECT client_id, product_type_id
FROM loans
UNION ALL SELECT client_id, product_type_id FROM products;

--EXISTS
SELECT log_type
FROM logs l
WHERE EXISTS
    (SELECT 'warning'
     FROM log_message m
     WHERE m.log_id = l.id AND log_message = 'warning')
ORDER BY log_type;

--INSERT INTO SELECT
INSERT INTO staff (user_id)
SELECT id
FROM users
WHERE user_role = 'staff' AND id NOT IN (
    SELECT user_id FROM staff
    );
SELECT * FROM staff;

--CASE
SELECT client_id,
       AVG(order_amount) AS average_order,
       CASE
        WHEN AVG(order_amount) <= 0
            THEN 'No credits'
        WHEN AVG(order_amount) > 0
            THEN 'Client has open credits'
       END loan_status
FROM loans
GROUP BY client_id
ORDER BY average_order;

--EXPLAIN
EXPLAIN SELECT * FROM loans;