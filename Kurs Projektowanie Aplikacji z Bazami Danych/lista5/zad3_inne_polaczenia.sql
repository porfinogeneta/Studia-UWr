-- --transaction isolation level repeatable read
-- BEGIN TRANSACTION
-- UPDATE dbo.liczby SET liczba=4
-- WAITFOR DELAY '00:00:02'
-- UPDATE dbo.liczby SET liczba=4
-- ROLLBACK TRANSACTION

-- -- transaction isolation level serializable
BEGIN TRANSACTION
insert liczby values(151)
WAITFOR DELAY '00:00:05'
insert liczby values(151)
ROLLBACK TRANSACTION


