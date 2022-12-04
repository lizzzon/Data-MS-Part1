INSERT INTO staff_roles (staff_role_name) VALUES ('helper');

INSERT INTO staff (user_id, staff_role_id) VALUES (
        1,
        1
        );

INSERT INTO product_types (product_type_name) VALUES ('Vacuum cleaner');

INSERT INTO products (company_id, product_type_id, product_name,
                      product_cost, product_amount) VALUES (
        1,
        1,
        'Philips w100',
        300.50,
        20
        );

INSERT INTO citizenships (citizenship_name) VALUES ('BLR');

INSERT INTO documents (citizenship_id, current_type, documents_number, issue_date,
                       expiration_date) VALUES (
        1,
        'passport',
        'MP567498',
        '2015-07-23',
        '2020-03-27'
        );

INSERT INTO countries (country_name) VALUES ('Belarus');

INSERT INTO cities (city_name) VALUES ('Minsk');

INSERT INTO clients (user_id, country_id, city_id, document_id, last_name,
                     first_name, middle_name, sex, birth_date, phone, address) VALUES (
        1,
        1,
        1,
        1,
        'Ivanov',
        'Ivan',
        'Ivanovich',
        'male',
        '1996-09-07',
        '+375298514567',
        'test address'
        );

INSERT INTO loans (client_id, company_id, product_id, loan_status, loan_type,
                   order_amount, credit_period, credit_rate, outstanding_loan_amount,
                   credit_datetime, last_change_datetime) VALUES (
        1,
        1,
        1,
        'created',
        'credit',
        1,
        250,
        9.5,
        255.50,
        '2014-12-07',
        '2022-05-20'
        );