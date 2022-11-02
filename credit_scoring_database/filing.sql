INSERT INTO users (email, username, user_password, user_role) VALUES (
        'qwerty@gmail.com',
        'qwerty',
        '12345',
        staff
        );
INSERT INTO users VALUES (
        'ponchik@mail.ru',
        'ponchik',
        '758305',
        staff
        );
INSERT INTO users VALUES (
        'ivanyshka@gmail.com',
        'ivan',
        '463832',
        client
        );
INSERT INTO users VALUES (
        'serega@gmail.com',
        'sergey',
        '5121221',
        client
        );
INSERT INTO users VALUES (
        '5element@gmail.com',
        '5element',
        '5ele000',
        company
        );
INSERT INTO users VALUES (
        'electrosila@mail.ru',
        'electrosila',
        'electro00sila0',
        company
        );

INSERT INTO staff_roles (staff_role_name) VALUES ('moder');
INSERT INTO staff_roles VALUES ('admin');
INSERT INTO staff_roles VALUES ('helper');

INSERT INTO staff (user_id, staff_role_id) VALUES (
        1,
        3
        );
INSERT INTO staff VALUES (
        2,
        1
        );

INSERT INTO product_types (product_type_name) VALUES ('Vacuum cleaner');
INSERT INTO product_types VALUES ('Hair dryer');
INSERT INTO product_types VALUES ('Computer');

INSERT INTO products (company_id, product_type_id, product_name,
                      product_cost, product_amount) VALUES (
        1,
        1,
        'Philips',
        300.50,
        20
        );
INSERT INTO products VALUES (
        1,
        2,
        'Hiaomi',
        99.50,
        30
        );
INSERT INTO products VALUES (
        1,
        2,
        'ASUS',
        99.50,
        30
        );

INSERT INTO citizenships (citizenship_name) VALUES ('BLR');
INSERT INTO citizenships VALUES ('RUS');
INSERT INTO citizenships VALUES ('US');

INSERT INTO documents (citizenship_id, current_type, documents_number, issue_date,
                       expiration_date) VALUES (
        1,
        passport,
        MP567498,
        23-07-2015,
        28-07-2020.
        );
INSERT INTO documents VALUES (
        2,
        residence,
        MK096054,
        12-10-2022,
        14-10-2024
        );

INSERT INTO countries (country_name) VALUES ('Belarus');
INSERT INTO countries VALUES ('Russia');
INSERT INTO countries VALUES ('United Kingdom');

INSERT INTO cities (city_name) VALUES ('Minsk');
INSERT INTO cities VALUES ('Moscow');
INSERT INTO cities VALUES ('London');

INSERT INTO companies (user_id, company_name, short_name) VALUES (
        5,
        '5 element',
        '5'
        );
INSERT INTO companies VALUES (
        6,
        'electrosila'
        );

INSERT INTO clients (user_id, country_id, city_id, document_id, last_name,
                     first_name, middle_name, sex, birth_date, phone, address) VALUES (
        3,
        1,
        1,
        1,
        'Ivanov',
        'Ivan',
        'Ivanovich',
        male,
        07-09-1996,
        '+375298514567'
        );
INSERT INTO clients VALUES (
        4,
        3,
        3,
        2,
        'Sergeev',
        'Sergey',
        'Sergeevich',
        male,
        15-12-1967,
        '+375298514567'
        );

INSERT INTO loans (client_id, company_id, product_id, loan_status, loan_type,
                   order_amount, credit_period, credit_rate, outstanding_loan_amount,
                   credit_datetime, last_change_datetime) VALUES (
        1,
        1,
        1,
        created,
        credit,
        1,
        14:35,
        9.5,
        255.50,
        07-12-2014,
        20-05-2022
        );
INSERT INTO loans VALUES (
        2,
        2,
        3,
        confirmed,
        installment,
        1,
        08:54,
        0,
        2090.50,
        05-08-2020,
        27-10-2024
        );

INSERT INTO logs (user_id, staff_role_id, log_type, log_message, time_stamp) VALUES (
        1,
        1,
        error,
        'error',
        current_timestamp
        );
INSERT INTO logs VALUES (
        2,
        3,
        warning,
        'warning',
        current_timestamp
        );