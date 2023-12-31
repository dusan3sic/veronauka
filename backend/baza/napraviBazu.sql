CREATE OR REPLACE DATABASE knjigaVencanih;
use knjigaVencanih;

CREATE OR REPLACE TABLE Osoba(
	id int NOT NULL,
    ime varchar(30),
    prezime varchar(30),
    zanimanje varchar(30),
    mestoRodjenja varchar(30),
    godinaRodjenja date,
    drzavljanstvo varchar(30),
    imePrezimeRoditelji varchar(30),
    primary key(id)
);


CREATE OR REPLACE TABLE Brak(
    idOsobe1 int NOT NULL,
    idOsobe2 int NOT NULL,
    
	brakSklopljen date,
	brakPoRedu int,
	mestoVencanja varchar(30),
	koJeVencao varchar(30),
	svedoci varchar(100),

    constraint fk_brak_osoba2 foreign key (idOsobe2) references Osoba(id),
    constraint fk_brak_osoba1 foreign key (idOsobe1) references Osoba(id),
    primary key(idOsobe1, idOsobe2, brakPoRedu)
);