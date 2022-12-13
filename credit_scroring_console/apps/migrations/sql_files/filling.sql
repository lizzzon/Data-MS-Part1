INSERT INTO users (email, username, user_password, user_role) VALUES (
        'liza@gmail.com',
        'liza',
        'liza_pass',
        'client'
        );
INSERT INTO users (email, username, user_password, user_role) VALUES (
        'ponchik@mail.ru',
        'ponchik',
        'superpass',
        'staff'
        );
INSERT INTO users (email, username, user_password, user_role) VALUES (
        'ivanyshka@gmail.com',
        'ivan',
        'superpass',
        'client'
        );
INSERT INTO users (email, username, user_password, user_role) VALUES (
        'serega@gmail.com',
        'sergey',
        'superpass',
        'client'
        );
INSERT INTO users (email, username, user_password, user_role) VALUES (
        '5element@gmail.com',
        '5element',
        'superpass',
        'company'
        );
INSERT INTO users (email, username, user_password, user_role) VALUES (
        'electrosila@mail.ru',
        'electrosila',
        'superpass',
        'company'
        );

INSERT INTO staff_roles (staff_role_name) VALUES ('moder');
INSERT INTO staff_roles (staff_role_name) VALUES ('admin');
INSERT INTO staff_roles (staff_role_name) VALUES ('helper');

INSERT INTO staff (user_id, staff_role_id) VALUES (
        1,
        3
);
INSERT INTO staff (user_id, staff_role_id) VALUES (
        2,
        1
);

INSERT INTO companies (user_id, company_name, short_name) VALUES (
        5,
        '5 element',
        '5'
);
INSERT INTO companies (user_id, company_name, short_name) VALUES (
        6,
        'electrosila',
        '6'
);


INSERT INTO product_types (product_type_name) VALUES ('Vacuum cleaner');
INSERT INTO product_types (product_type_name) VALUES ('Hair dryer');
INSERT INTO product_types (product_type_name) VALUES ('Computer');

INSERT INTO products (company_id, product_type_id, product_name,
                      product_cost, product_amount) VALUES (
        1,
        1,
        'Philips w100',
        300.50,
        20
        );
INSERT INTO products (company_id, product_type_id, product_name,
                      product_cost, product_amount) VALUES (
        2,
        2,
        'Hiaomi redmi',
        99.50,
        30
        );
INSERT INTO products (company_id, product_type_id, product_name,
                      product_cost, product_amount) VALUES (
        1,
        2,
        'ASUS zenbook',
        99.50,
        30
        );

INSERT INTO citizenships (citizenship_name) VALUES ('BLR');
INSERT INTO citizenships (citizenship_name) VALUES ('RUS');
INSERT INTO citizenships (citizenship_name) VALUES ('US');

INSERT INTO documents (citizenship_id, current_type, documents_number, issue_date,
                       expiration_date) VALUES (
        1,
        'passport',
        'MP567498',
        '2015-07-23',
        '2020-03-27'
        );
INSERT INTO documents (citizenship_id, current_type, documents_number, issue_date,
                       expiration_date) VALUES (
        2,
        'residence',
        'MK096054',
        '2022-10-12',
        '2024-10-14'
        );

INSERT INTO countries (country_name) VALUES ('Belarus');
INSERT INTO countries (country_name) VALUES ('Russia');
INSERT INTO countries (country_name) VALUES ('United Kingdom');

INSERT INTO cities (city_name) VALUES ('Minsk');
INSERT INTO cities (city_name) VALUES ('Moscow');
INSERT INTO cities (city_name) VALUES ('London');

INSERT INTO clients (user_id, country_id, city_id, document_id, last_name,
                     first_name, middle_name, sex, birth_date, phone, address) VALUES (
        3,
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
INSERT INTO clients (user_id, country_id, city_id, document_id, last_name,
                     first_name, middle_name, sex, birth_date, phone, address) VALUES (
        4,
        3,
        3,
        2,
        'Sergeev',
        'Sergey',
        'Sergeevich',
        'male',
        '1967-12-15',
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
INSERT INTO loans (client_id, company_id, product_id, loan_status, loan_type,
                   order_amount, credit_period, credit_rate, outstanding_loan_amount,
                   credit_datetime, last_change_datetime) VALUES (
        2,
        2,
        3,
        'confirmed',
        'installment',
        1,
        360,
        0,
        2090.50,
        '2020-08-05',
        '2024-10-27'
        );