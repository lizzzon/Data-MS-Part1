--PROCEDURES

CREATE OR REPLACE PROCEDURE change_client_name(current_user_id int, new_name varchar)
LANGUAGE plpgsql AS $$
BEGIN
 UPDATE clients
    SET first_name = new_name
    WHERE id = current_user_id;
END;
$$;


CREATE OR REPLACE PROCEDURE change_company_name(current_user_id int, new_name varchar)
LANGUAGE plpgsql AS $$
BEGIN
 UPDATE companies
    SET company_name = new_name
    WHERE id = current_user_id;
END;
$$;


CREATE OR REPLACE PROCEDURE insert_person()
LANGUAGE plpgsql AS $$
BEGIN
 INSERT INTO {table}
     {keys} VALUES {values};
END;
$$;