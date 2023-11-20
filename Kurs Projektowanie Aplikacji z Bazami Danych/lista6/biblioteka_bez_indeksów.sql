DROP TABLE IF EXISTS dbo.Wypozyczenie_idx;
GO

DROP TABLE IF EXISTS dbo.Egzemplarz_idx;
GO

DROP TABLE IF EXISTS dbo.Czytelnik_idx;
GO

DROP TABLE IF EXISTS dbo.Ksiazka_idx;
GO

CREATE TABLE dbo.Ksiazka_idx
( Ksiazka_ID INT IDENTITY
, ISBN VARCHAR(20)
, Tytul VARCHAR(300)
, Autor VARCHAR(200)
, Rok_Wydania INT
, Cena DECIMAL(10,2)
, Wypozyczona_Ostatni_Miesiac BIT
-- , CONSTRAINT Ksiazka_PK PRIMARY KEY (Ksiazka_ID)
-- , CONSTRAINT Ksiazka_UK_ISBN UNIQUE (ISBN)
);
GO

CREATE TABLE dbo.Egzemplarz_idx
( Egzemplarz_ID INT IDENTITY
, Sygnatura CHAR(8)
, Ksiazka_ID INT
-- , CONSTRAINT Egzemplarz_PK PRIMARY KEY (Egzemplarz_ID)
-- , CONSTRAINT Egzemplarz_UK_Sygnatura UNIQUE (Sygnatura)
-- , CONSTRAINT Egzemplarz_FK FOREIGN KEY (Ksiazka_ID) REFERENCES Ksiazka (Ksiazka_ID) ON DELETE CASCADE
);
GO

CREATE TABLE dbo.Czytelnik_idx
( Czytelnik_ID INT IDENTITY
, PESEL CHAR(11)
, Nazwisko VARCHAR(30)
, Miasto VARCHAR(30)
, Data_Urodzenia DATE
, Ostatnie_Wypozyczenie DATE
-- , CONSTRAINT Czytelnik_PK PRIMARY KEY (Czytelnik_ID)
-- , CONSTRAINT Czytelnik_UK_PESEL UNIQUE (PESEL)
);
GO

CREATE TABLE dbo.Wypozyczenie_idx
( Wypozyczenie_ID INT IDENTITY
, Czytelnik_ID INT
, Egzemplarz_ID INT
, Data DATE
, Liczba_Dni INT
-- , CONSTRAINT Wypozyczenie_PK PRIMARY KEY (Wypozyczenie_ID)
-- , CONSTRAINT Wypozyczenie_FK_Czytelnik FOREIGN KEY (Czytelnik_ID) REFERENCES Czytelnik (Czytelnik_ID) ON DELETE CASCADE
-- , CONSTRAINT Wypozyczenie_FK_Egzemplarz FOREIGN KEY (Egzemplarz_ID) REFERENCES Egzemplarz (Egzemplarz_ID) ON DELETE CASCADE
);
GO

SET IDENTITY_INSERT dbo.Ksiazka_idx ON
INSERT INTO dbo.Ksiazka_idx (Ksiazka_ID,ISBN,Tytul,Autor,Rok_Wydania,Cena) VALUES
(1,'83-246-0279-8','Microsoft Access. Podrêcznik administratora','Helen Feddema',2006,69),
(2,'83-246-0653-X','SQL Server 2005. Programowanie. Od podstaw','Robert Vieira',2007,97),
(3,'978-83-246-0549-1','SQL Server 2005. Wycinij wszystko','Eric L. Brown',2007,57),
(4,'978-83-246-1258-1','PHP, MySQL i MVC. Tworzenie witryn WWW opartych na bazie danych','W³odzimierz Gajda',2010,79),
(5,'978-83-246-2060-9','Access 2007 PL. Seria praktyk','Andrew Unsworth',2009,39),
(6,'978-83-246-2188-0','Czysty kod. Podrêcznik dobrego programisty','Robert C. Martin',2010,67);
SET IDENTITY_INSERT dbo.Ksiazka_idx OFF
GO

SET IDENTITY_INSERT dbo.Egzemplarz_idx ON
INSERT INTO dbo.Egzemplarz_idx (Egzemplarz_ID,Ksiazka_ID,Sygnatura) VALUES
(1,5,'S0001'),
(2,5,'S0002'),
(3,1,'S0003'),
(4,1,'S0004'),
(5,1,'S0005'),
-- (6,2,'S0006'),
(7,3,'S0007'),
(8,3,'S0008'),
(9,3,'S0009'),
(10,3,'S0010'),
(11,6,'S0011'),
(12,6,'S0012'),
(13,4,'S0013'),
(14,4,'S0014'),
(15,4,'S0015');
SET IDENTITY_INSERT dbo.Egzemplarz_idx OFF
GO

SET IDENTITY_INSERT dbo.Czytelnik_idx ON
INSERT INTO dbo.Czytelnik_idx (CZYTELNIK_ID,PESEL,NAZWISKO,MIASTO,DATA_URODZENIA) VALUES
(1,'55101011111','Kowalski','Wroc³aw','1955-10-10'),
(2,'60101033333','Maliniak','Wroc³aw','1960-10-10'),
(3,'65120122222','Nowak','Warszawa','1965-12-01');
SET IDENTITY_INSERT dbo.Czytelnik_idx OFF
GO

SET IDENTITY_INSERT dbo.Wypozyczenie_idx ON
INSERT INTO dbo.Wypozyczenie_idx (Wypozyczenie_ID,Czytelnik_ID,Egzemplarz_ID,Data,Liczba_Dni) VALUES
(1,1,3,'2020-02-01',12),
(2,1,4,'2020-01-05',20),
(3,1,15,'2020-01-21',45),
(4,2,8,'2020-01-13',7),
(5,3,4,'2020-02-01',14),
(6,3,12,'2020-02-02',10),
(7,3,12,'2020-02-12',3),
(8,3,12,'2020-02-16',4),
(9,1,12,'2020-02-20',2),
(10,2,12,'2020-02-22',5),
(11,2,12,'2020-02-28',12),
(12,1,12,'2020-03-10',8),
(13,3,12,'2020-03-15',4);
SET IDENTITY_INSERT dbo.Wypozyczenie_idx OFF
GO
