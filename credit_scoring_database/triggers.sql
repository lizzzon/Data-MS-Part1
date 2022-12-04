CREATE OR REPLACE FUNCTION user_insert() RETURNS event_trigger AS $Users_Insert$
BEGIN
    RAISE NOTICE 'Add user: ', username;
END;
$Users_Insert$ LANGUAGE plpgsql;

CREATE EVENT TRIGGER user_insert ON ddl_command_start EXECUTE PROCEDURE user_insert();