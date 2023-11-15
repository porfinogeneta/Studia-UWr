-- lock hints to opcje, które dodajemy w przypdaku query po dane, 
-- żeby te dane przeszukiwać w odpowiedni sposób
-- NOLOCK - umożliwia czytanie z tabelki, nawet jeśli nie była ona COMMITED,
-- używanie go zapobiega powstawaniu DEADLOCK'ÓW i zużywa mniej pamięci

-- najlepiej używaż z WITH (można różne locki pododawać)
DROP TABLE IF EXISTS brands
GO
CREATE TABLE brands(name VARCHAR(15), value INT)
GO
INSERT INTO brands(name, value) VALUES ('Seat', 12), ('Mercedes', 15), ('Volvo', 10)
GO

SET TRANSACTION ISOLATION LEVEL SERIALIZABLE
BEGIN TRANSACTION 
UPDATE brands
SET [value] = 20
FROM brands
WHERE [name] = 'Seat'
-- tu powinien być commit, ale go omijamy, co powoduje w query, nieskońcozne zapytanie w naszym query

