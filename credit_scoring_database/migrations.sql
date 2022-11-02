CREATE TYPE roles AS ENUM ('staff', 'client', 'company');
CREATE TYPE sex AS ENUM ('male', 'female');
CREATE TYPE types AS ENUM ('passport', 'residence', 'permit');
CREATE TYPE loan_status AS ENUM ('created', 'confirmed', 'issued', 'redeemed', 'overdue');
CREATE TYPE loan_type AS ENUM ('installment', 'credit');
CREATE TYPE log_type AS ENUM ('error', 'warning', 'info');

CREATE TABLE users (
    id              int PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    email           varchar(64) UNIQUE NOT NULL,
    username        varchar(16) UNIQUE NOT NULL,
    user_password   varchar(32) UNIQUE NOT NULL,
    user_role       roles
);

CREATE TABLE staff_roles (
    id                  int PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    staff_role_name     varchar(16) NOT NULL
);

CREATE TABLE staff (
    id              int PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    user_id         int,
    staff_role_id   int,
    CONSTRAINT fk_user
        FOREIGN KEY(user_id)
            REFERENCES users(id),
    CONSTRAINT fk_staff_roles
        FOREIGN KEY(staff_role_id)
            REFERENCES staff_roles(id)
);

CREATE TABLE logs (
    id              int PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    user_id         int,
    staff_role_id   int,
    log_type        log_type NOT NULL,
    log_message     varchar(64),
    time_stamp      timestamp,
    CONSTRAINT fk_user
        FOREIGN KEY(user_id)
            REFERENCES users(id),
    CONSTRAINT fk_staff
        FOREIGN KEY(staff_role_id)
            REFERENCES staff_roles(id)
);
CREATE TABLE countries (
    id              int PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    country_name    varchar(32) NOT NULL
);

CREATE TABLE cities (
    id              int PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    city_name       varchar(32) NOT NULL
);

CREATE TABLE citizenships (
    id                  int PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    citizenship_name    varchar(4) NOT NULL
);

CREATE TABLE documents (
    id                  int PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    citizenship_id      int,
    current_type        types NOT NULL,
    documents_number    char NOT NULL,
    issue_date          date,
    expiration_date     date,
    CONSTRAINT fk_citizenship
        FOREIGN KEY(citizenship_id)
            REFERENCES citizenships(id)
);

CREATE TABLE clients (
    id              int PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    user_id         int,
    country_id      int,
    city_id         int,
    document_id     int,
    last_name       varchar(32) NOT NULL,
    first_name      varchar(32) NOT NULL,
    middle_name     varchar(32),
    sex             sex NOT NULL,
    birth_date      date NOT NULL,
    phone           varchar(16) NOT NULL,
    address         varchar(64) NOT NULL,
    CONSTRAINT fk_user
        FOREIGN KEY(user_id)
            REFERENCES users(id),
    CONSTRAINT fk_country
        FOREIGN KEY(country_id)
            REFERENCES countries(id),
    CONSTRAINT fk_city
        FOREIGN KEY(city_id)
            REFERENCES cities(id),
    CONSTRAINT fk_document
        FOREIGN KEY(document_id)
            REFERENCES documents(id)
);

CREATE TABLE companies (
    id               int PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    user_id          int,
    company_name     varchar(32) NOT NULL,
    short_name       varchar(32),
    CONSTRAINT fk_user
        FOREIGN KEY(user_id)
            REFERENCES users(id)
);

CREATE TABLE product_types (
    id                  int PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    product_type_name   varchar(32) NOT NULL
);

CREATE TABLE products (
    id                  int PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    company_id          int,
    product_type_id     int,
    product_name        varchar(32) NOT NULL,
    product_cost        decimal NOT NULL,
    product_amount      int NOT NULL,
    CONSTRAINT fk_company
        FOREIGN KEY(company_id)
            REFERENCES companies(id),
    CONSTRAINT fk_product_type
        FOREIGN KEY(product_type_id)
            REFERENCES product_types(id)
);

CREATE TABLE loans (
    id                          int PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    client_id                   int,
    company_id                  int,
    product_id                  int,
    loan_status                 loan_status NOT NULL,
    loan_type                   loan_type NOT NULL,
    order_amount                int NOT NULL,
    credit_period               date,
    credit_rate                 decimal,
    outstanding_loan_amount     decimal NOT NULL,
    credit_datetime             timestamp NOT NULL,
    last_change_datetime        timestamp NOT NULL,
    CONSTRAINT fk_client
        FOREIGN KEY(client_id)
            REFERENCES clients(id),
    CONSTRAINT fk_company
        FOREIGN KEY(company_id)
            REFERENCES companies(id),
    CONSTRAINT fk_product
        FOREIGN KEY(product_id)
            REFERENCES products(id)
);