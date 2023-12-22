DELIMITER //

CREATE OR REPLACE PROCEDURE print(IN p_message int)
BEGIN
    -- Raise a condition to capture and output the message
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = p_message;
END //

DELIMITER ;