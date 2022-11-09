TRUNCATE companies_id_seq, countries_id_seq,
    documents_id_seq, loans_id_seq, logs_id_seq, product_types_id_seq, cities_id_seq, products_id_seq,
    staff_id_seq, staff_roles_id_seq, users_id_seq RESTART IDENTITY;

DROP TABLE users, cities, citizenships, clients, companies, countries, documents,
    loans, logs, product_types, products, staff, staff_roles CASCADE;

DROP TYPE loan_status, loan_type, roles, sex, types, log_type CASCADE;