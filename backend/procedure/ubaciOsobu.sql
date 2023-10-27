DELIMITER //

CREATE OR REPLACE PROCEDURE ubaciOsobu(IN ime varchar(30), IN prezime varchar(30))
BEGIN
    insert into Osoba(ime, prezime)
    values (ime, prezime);
END //

DELIMITER ;