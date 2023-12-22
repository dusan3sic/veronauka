DELIMITER //

CREATE OR REPLACE PROCEDURE ubaciOsobu(
    IN p_ime varchar(30),
    IN p_prezime varchar(30),
    IN p_zanimanje varchar(30),
    IN p_mestoRodjenja varchar(30),
    IN p_godinaRodjenja date,
    IN p_drzavljanstvo varchar(30),
    IN p_imePrezimeRoditelji varchar(30),
    OUT p_inserted_id INT
)
BEGIN
    DECLARE id INT;

    SELECT max(Osoba.id) INTO id
    FROM Osoba
    WHERE Osoba.ime = p_ime AND Osoba.prezime = p_prezime AND Osoba.godinaRodjenja = p_godinaRodjenja;

    if id is null then
        SELECT COALESCE(MAX(Osoba.id), 0) + 1 INTO id FROM Osoba;

        INSERT INTO Osoba(id, ime, prezime, zanimanje, mestoRodjenja, godinaRodjenja, drzavljanstvo, imePrezimeRoditelji)
        VALUES (id, p_ime, p_prezime, p_zanimanje, p_mestoRodjenja, p_godinaRodjenja, p_drzavljanstvo, p_imePrezimeRoditelji);

    end if;
    
    SET p_inserted_id = id;

END //

DELIMITER ;