-- TRIGGERS
CREATE OR REPLACE FUNCTION user_insert_logs()
RETURNS TRIGGER AS $logging$
    BEGIN
        IF (TG_OP = 'INSERT') THEN
            INSERT INTO logs SELECT 'Inserting user', NEW.id, now();
            RETURN NEW;
        END IF;
        RETURN NULL;
    END;
$logging$ LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER insert_logging
AFTER INSERT ON users
FOR EACH ROW EXECUTE FUNCTION user_insert_logs();


CREATE OR REPLACE FUNCTION user_delete_logs()
RETURNS TRIGGER AS $logging$
    BEGIN
        IF (TG_OP = 'DELETE') THEN
            INSERT INTO logs SELECT 'Deleting user', OLD.id, now();
            RETURN OLD;
        END IF;
        RETURN NULL; -- возвращаемое значение для триггера AFTER игнорируется
    END;
$logging$ LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER delete_logging
BEFORE DELETE ON users
FOR EACH ROW EXECUTE FUNCTION user_delete_logs();