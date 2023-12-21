DELIMITER //

CREATE OR REPLACE PROCEDURE sklopiBrak(
    IN idOsobe1 int, IN idOsobe2 int, IN brakSklopljen date, 
    IN brakPoRedu int, IN mestoVencanja varchar(30), 
    IN koJeVencao varchar(30), IN svedoci varchar(100)
)
BEGIN
    insert into Brak 
    values (
        idOsobe1,
        idOsobe2, 
        brakSklopljen, 
        brakPoRedu,
        mestoVencanja,
        koJeVencao,
        svedoci
    );
END //

DELIMITER ;