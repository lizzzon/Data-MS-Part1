UPDATE staff_roles
SET staff_role_name = 'role_name'
WHERE id = 1;

UPDATE staff
SET staff_role_id = 'staff_id'
WHERE id = 1;

UPDATE products
SET product_name = 'product_name',
    product_cost = 'product_cost',
    product_amount = 'product_amount'
WHERE id = 1;

UPDATE product_types
SET product_type_name = 'product_type_name'
WHERE id = 1;

UPDATE logs
SET log_type = 'log_type',
    log_message = 'log_message',
    time_stamp = 'time_stamp'
WHERE id = 1;

UPDATE loans
SET loan_status = 'loan_status',
    loan_type = 'loan_type',
    order_amount = 'order_amount',
    credit_period = 'credit_period',
    credit_rate = 'credit_rate',
    outstanding_loan_amount = 'outstanding_loan_amount',
    credit_datetime = 'credit_datetime',
    last_change_datetime = 'last_change_datetime'
WHERE id = 1;

UPDATE documents
SET current_type = 'current_type',
    documents_number = 'documents_number',
    issue_date = 'issue_date',
    expiration_date = 'expiration_date'
WHERE id = 1;

UPDATE countries
SET country_name = 'country_name'
WHERE id = 1;

UPDATE companies
SET company_name = 'company_name',
    short_name = 'short_name'
WHERE id = 1;

UPDATE clients
SET last_name = 'last_name',
    first_name = 'first_name',
    middle_name = 'middle_name',
    sex = 'sex',
    birth_date = 'birth_date',
    phone = 'phone',
    address = 'address'
WHERE id = 1;

UPDATE citizenships
SET citizenship_name = 'citizenship_name'
WHERE id = 1;

UPDATE cities
SET city_name = 'city_name'
WHERE id = 1;