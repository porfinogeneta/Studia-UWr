-- usuwanie jak już użyliśmy tej nazwy
IF OBJECT_ID('Test1', 'U') IS NOT NULL
    DROP TABLE Test1;

-- tabela z wartościami IDENTITY
CREATE TABLE Test1
(
    ID INT IDENTITY(1000, 10) PRIMARY KEY,
    Data VARCHAR(255)
);
-- kod tworzący Test
-- CREATE TABLE Test
-- (
--     ID INT IDENTITY(1000, 10) PRIMARY KEY,
--     Data VARCHAR(255)
-- );
-- dodanie danych
INSERT INTO Test1 (Data) VALUES ('Row 1');
INSERT INTO Test1 (Data) VALUES ('Row 2');
INSERT INTO Test1 (Data) VALUES ('Row 3');

-- @@IDENTITY pobiera klucz ostatniego rzędu w danym okienku
-- IDENT_CURRENT - w całym projekcie
-- SELECT @@IDENTITY AS '@@IDENTITY',
-- zwraca ostatnie Identity wygenerowane dla podanej tabelki, nie koniecznie w danym zakresie
-- @@IDENTITY klucz ostatniego Inserta w danym Scope
-- IDENT_CURRENT - ostatni klucz dla danej tabelki, zakres jest bez znaczenia
SELECT @@IDENTITY AS '@@IDENTITY',
IDENT_CURRENT('Test') AS 'IDENT_CURRENT'; -- Test istnieje już gdzieś i zaczyna się od 1000, nie nie zostało do niego dodane
