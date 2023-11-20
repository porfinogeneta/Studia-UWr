DROP TABLE IF EXISTS Cars
GO

CREATE TABLE Cars(
    ID INT PRIMARY KEY IDENTITY(1,1),
    Brand VARCHAR(20),
    Age INT
)
GO

INSERT INTO Cars(Brand, Age) VALUES ('Seat', 10), ('Mazda', 15), ('Saab', 25), ('Tesla', 3)
GO

-- DRITY READ zmieniamy dane, później tą zmianę wycofujemy, ale odczytujemy złe w naszym query
-- BEGIN TRANSACTION
-- UPDATE Cars SET Brand = 'Mercedes' WHERE ID = 3
-- WAITFOR DELAY '00:00:05'
-- ROLLBACK TRANSACTION

-- NON REPEATABLE
-- BEGIN TRANSACTION
-- UPDATE Cars SET Age = 12 WHERE Age <= 15
-- WAITFOR DELAY '00:00:05'
-- ROLLBACK TRANSACTION

-- PHANTOM READ
BEGIN TRANSACTION
INSERT INTO Cars (Brand, Age) VALUES ('Lamborghini', 1)
WAITFOR DELAY '00:00:03'
ROLLBACK TRANSACTION