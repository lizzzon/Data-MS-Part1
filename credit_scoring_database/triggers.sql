-- TRIGGERS
CREATE OR REPLACE FUNCTION user_logs()
RETURNS TRIGGER AS $logging$
DECLARE log_msg varchar;
DECLARE role_nm varchar;
    BEGIN
        IF (TG_OP = 'DELETE') THEN
            log_msg := 'Delete user';
            role_nm := 'moder';
        ELSIF (TG_OP = 'UPDATE') THEN
            log_msg := 'Update user';
            role_nm := 'moder';
        ELSIF (TG_OP = 'INSERT') THEN
            log_msg := 'Insert user';
            role_nm := 'moder';
        END IF;
        INSERT INTO logs (user_id, staff_role_id, log_type, log_message, time_stamp)
        VALUES (NEW.id, (SELECT id FROM staff_roles WHERE staff_role_name = role_nm), 'info', log_msg, now());
        RETURN NULL;
    END;
$logging$ LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER user_logging_trigger
AFTER INSERT ON users
FOR EACH ROW EXECUTE FUNCTION user_logs();