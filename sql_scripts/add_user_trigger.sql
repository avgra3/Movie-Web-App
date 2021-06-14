/* Creating an update trigger for when one table is updated, so will the other */
DROP TRIGGER IF EXISTS new_user_trigger;

-- Creating the trigger
-- Works to add users who have registered.
CREATE TRIGGER new_user_trigger
	AFTER UPDATE ON auth_user
	FOR EACH ROW
	-- Inserts the default image 
	-- and the new registered ID
	INSERT INTO users_profile(image, user_id)
		VALUES('default.jpg', NEW.id);
-- If you see the trigger, then you have
-- successfully added the trigger
SHOW TRIGGERS IN movies;