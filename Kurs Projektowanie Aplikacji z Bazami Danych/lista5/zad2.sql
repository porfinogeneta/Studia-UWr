/*
DIRTY READ - czytanie nie zacommitowanych danych
*/

-- odczyt zupdatowanych na chwilę danych
-- SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED
-- SELECT * FROM dbo.Cars


-- NON REPEATABLE - jest wtedy, gdy w tym samym zakresie transakcji czytamy dane dwa razy
-- ale otrzymujemy inne wyniki przez zmiany w tych danych
-- SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED
-- SELECT * FROM dbo.Cars AS C
-- WHERE C.Age <= 12

-- WAITFOR DELAY '00:00:05'

-- SELECT * FROM dbo.Cars AS C
-- WHERE C.Age <= 12

-- PHANTOM READ - jest wtedy, gdy odczytujemy dane, do których coś dodaliśmy, ale cofamy to dodanie
-- SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED
-- SELECT * FROM dbo.Cars

-- WAITFOR DELAY '00:00:08'

-- SELECT * FROM dbo.Cars