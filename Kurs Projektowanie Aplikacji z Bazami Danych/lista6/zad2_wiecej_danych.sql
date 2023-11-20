-- Add 10 more Czytelnik
SET IDENTITY_INSERT Czytelnik ON
INSERT INTO Czytelnik (Czytelnik_ID, PESEL, NAZWISKO, MIASTO, DATA_URODZENIA) VALUES
(4, '72123144444', 'Nowicki', 'Kraków', '1972-12-31'),
(5, '80111555555', 'Wójcik', 'Gdańsk', '1980-11-15'),
(6, '88121266666', 'Lis', 'Poznań', '1988-12-12'),
(7, '95050577777', 'Kamiński', 'Łódź', '1995-05-05'),
(8, '92020288888', 'Szymański', 'Katowice', '1992-02-02'),
(9, '84070799999', 'Duda', 'Szczecin', '1984-07-07'),
(10, '89080810101', 'Kaczmarek', 'Bydgoszcz', '1989-08-08'),
(11, '93030311222', 'Górski', 'Rzeszów', '1993-03-03'),
(12, '78080812345', 'Olszewski', 'Gdynia', '1978-08-08'),
(13, '87070723456', 'Jaworski', 'Białystok', '1987-07-07');
SET IDENTITY_INSERT Czytelnik OFF

-- Add 30 more Egzemplarz
SET IDENTITY_INSERT Egzemplarz ON
INSERT INTO Egzemplarz (Egzemplarz_ID, Ksiazka_ID, Sygnatura) VALUES
(16, 2, 'S0016'),
(17, 2, 'S0017'),
(18, 2, 'S0018'),
(19, 2, 'S0019'),
(20, 3, 'S0020'),
(21, 3, 'S0021'),
(22, 3, 'S0022'),
(23, 4, 'S0023'),
(24, 4, 'S0024'),
(25, 4, 'S0025'),
(26, 5, 'S0026'),
(27, 5, 'S0027'),
(28, 5, 'S0028'),
(29, 6, 'S0029'),
(30, 6, 'S0030'),
(31, 6, 'S0031'),
(32, 6, 'S0032'),
(33, 6, 'S0033'),
(34, 6, 'S0034'),
(35, 6, 'S0035');
SET IDENTITY_INSERT Egzemplarz OFF

-- Add 20 more Wypozyczenie
SET IDENTITY_INSERT Wypozyczenie ON
INSERT INTO Wypozyczenie (Wypozyczenie_ID, Czytelnik_ID, Egzemplarz_ID, Data, Liczba_Dni) VALUES
(14, 4, 16, '2020-03-20', 10),
(15, 5, 18, '2020-03-25', 15),
(16, 6, 20, '2020-04-01', 8),
(17, 7, 22, '2020-04-05', 5),
(18, 8, 24, '2020-04-10', 12),
(19, 9, 26, '2020-04-15', 7),
(20, 10, 28, '2020-04-20', 14),
(23, 2, 25, '2020-05-05', 22),
(25, 4, 27, '2020-05-15', 11),
(26, 5, 28, '2020-05-20', 16),
(27, 6, 29, '2020-05-25', 13),
(28, 7, 30, '2020-06-01', 19),
(29, 8, 31, '2020-06-05', 24),
(30, 9, 32, '2020-06-10', 8),
(31, 10, 33, '2020-06-15', 12),
(32, 1, 34, '2020-06-20', 15),
(33, 2, 35, '2020-06-25', 21);
SET IDENTITY_INSERT Wypozyczenie OFF

-- Add 10 more Ksiazka
SET IDENTITY_INSERT Ksiazka ON
INSERT INTO Ksiazka (Ksiazka_ID, ISBN, Tytul, Autor, Rok_Wydania, Cena, Wypozyczona_Ostatni_Miesiac) VALUES
(7, '978-83-246-3456-7', 'Python Programming', 'John Smith', 2022, 49.99, 0),
(8, '978-83-246-9876-5', 'Machine Learning Basics', 'Alice Johnson', 2021, 59.99, 1),
(9, '978-83-246-1111-1', 'Web Development with React', 'David Brown', 2020, 39.99, 0),
(10, '978-83-246-2222-2', 'Data Science Essentials', 'Emily White', 2019, 79.99, 1),
(11, '978-83-246-4444-4', 'Java in Action', 'Michael Miller', 2018, 29.99, 0),
(12, '978-83-246-5555-5', 'C# Programming Guide', 'Sophie Turner', 2017, 69.99, 1),
(13, '978-83-246-6666-6', 'Networking Fundamentals', 'Daniel Wilson', 2016, 49.99, 0),
(14, '978-83-246-7777-7', 'Cybersecurity Basics', 'Olivia Martinez', 2015, 89.99, 1),
(15, '978-83-246-8888-8', 'Android App Development', 'William Davis', 2014,59.99, 0),
(16, '978-83-246-9999-9', 'iOS Development Essentials', 'Emma Clark', 2013, 79.99, 1);
SET IDENTITY_INSERT Ksiazka OFF

