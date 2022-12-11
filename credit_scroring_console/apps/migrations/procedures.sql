--PROCEDURES

CREATE OR REPLACE PROCEDURE change_client_name(user_id int, new_name varchar)
LANGUAGE plpgsql AS $$
BEGIN
 UPDATE clients
    SET first_name = new_name
    WHERE id = user_id;
END;
$$;


CREATE OR REPLACE PROCEDURE change_company_name(user_id int, new_name varchar)
LANGUAGE plpgsql AS $$
BEGIN
 UPDATE companies
    SET company_name = new_name
    WHERE id = user_id;
END;
$$;