-- PROCEDURES

CREATE OR REPLACE PROCEDURE insert_user(curr_email varchar, curr_username varchar, curr_user_password varchar, curr_user_role roles)
LANGUAGE plpgsql AS $$
BEGIN
    INSERT INTO users (email, username, user_password, user_role)
    VALUES (curr_email, curr_username, curr_user_password, curr_user_role);
END;
$$;

CREATE OR REPLACE FUNCTION get_user(curr_username varchar)
RETURNS SETOF users AS $$
BEGIN
    RETURN QUERY SELECT * FROM users
    WHERE username = curr_username;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE PROCEDURE change_user_active(current_user_id int, curr_active bool)
LANGUAGE plpgsql AS $$
BEGIN
 UPDATE users
    SET is_active = curr_active
    WHERE id = current_user_id;
END;
$$;
