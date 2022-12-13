--Request with multiple conditions
SELECT * FROM users
WHERE email LIKE '%@mail.ru' AND user_role = 'staff'
ORDER BY username ASC;

--Query with nested construct
SELECT phone,
    (SELECT username FROM users
     WHERE email LIKE 'ponchik@mail.ru')
FROM clients;

--INNER JOIN
SELECT companies.company_name, product_types.product_type_name, products.product_name,
    products.product_cost, products.product_amount
FROM products
INNER JOIN product_types ON products.product_type_id = product_types.id
INNER JOIN companies ON products.company_id = companies.id;

SELECT clients.last_name, clients.first_name, companies.company_name, products.product_name,
    products.product_cost, loans.loan_status, loans.loan_type, loans.order_amount,
    loans.credit_period, loans.credit_rate
FROM loans
INNER JOIN clients ON loans.client_id = clients.id
INNER JOIN companies ON loans.company_id = companies.id
INNER JOIN products ON loans.product_id = products.id
WHERE loan_status = 'created' OR loan_status = 'confirmed' OR loan_status = 'issued';

SELECT citizenships.citizenship_name, documents.current_type, documents.documents_number,
    documents.issue_date, documents.exipration_date
FROM documents
INNER JOIN citizenships ON documents.citizenship_id = citizenships.id;

SELECT users.username, countries.country_name, cities.city_name, clients.last_name,
       clients.first_name, clients.middle_name, clients.sex, clients.birth_date,
       clients.phone, clients.address
FROM clients
INNER JOIN users ON clients.user_id = users.id
INNER JOIN countries ON clients.country_id = countries.id
INNER JOIN city ON clients.city_id = cities.id;

SELECT users.username, users.email, countries.country_name, cities.city_name,
       documents.current_type, clients.last_name, clients.first_name,
       clients.sex, clients.birth_date, clients.phone, clients.address
FROM clients
INNER JOIN users ON clients.user_id = users.id
INNER JOIN countries ON clients.country_id = countries.id
INNER JOIN cities ON clients.city_id = cities.id
INNER JOIN documents ON clients.document_id = documents.id;

SELECT users.username, users.email, staff_roles.staff_role_name
FROM staff
INNER JOIN users ON staff.user_id = users.id
INNER JOIN staff_roles ON staff.staff_role_id = staff_roles.id;

--OUTER JOIN
--LEFT
SELECT products.product_name, product_types.product_type_name
FROM products
LEFT JOIN product_types ON products.product_type_id = product_types.id;

--RIGHT
SELECT products.product_name, product_types.product_type_name
FROM products
RIGHT JOIN product_types ON products.product_type_id = product_types.id;

--FULL
SELECT clients.first_name, clients.last_name
FROM clients
FULL JOIN loans ON clients.id = loans.client_id;

--CROSS JOIN
SELECT * FROM users CROSS JOIN staff;

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
SELECT client_id, product_id
FROM loans
UNION ALL SELECT company_id, product_type_id FROM products;

--EXISTS
SELECT log_type
FROM logs l
WHERE EXISTS
    (SELECT log_message
     FROM logs m
     WHERE m.id = l.id AND log_message = 'problem')
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