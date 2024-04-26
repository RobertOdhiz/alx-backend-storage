-- Creates a trigger that resets attr valid_email only when the email is changed

DELIMITER $$;
CREATE TRIGGER email_change BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
	IF NEW.email != OLD.email THEN
		SET NEW.valid_email = 0;
	END IF;
END;
DELIMITER ;
