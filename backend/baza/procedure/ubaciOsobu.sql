DELIMITER //

CREATE OR REPLACE PROCEDURE ubaciOsobu(
    IN p_ime varchar(30),
    IN p_prezime varchar(30),
    IN p_zanimanje varchar(30),
    IN p_mestoRodjenja varchar(30),
    IN p_godinaRodjenja date,
    IN p_drzavljanstvo varchar(30),
    IN p_imePrezimeRoditelji varchar(30)
)
BEGIN

    DECLARE id INT;

    SELECT (MAX(Osoba.id) + 1) INTO id FROM Osoba;
    
    INSERT INTO Osoba(id, ime, prezime, zanimanje, mestoRodjenja, godinaRodjenja, drzavljanstvo, imePrezimeRoditelji)
    VALUES (id, p_ime, p_prezime, p_zanimanje, p_mestoRodjenja, p_godinaRodjenja, p_drzavljanstvo, p_imePrezimeRoditelji);

    SELECT id;

END //

DELIMITER ;