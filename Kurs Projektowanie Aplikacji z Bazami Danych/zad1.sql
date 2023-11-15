/*
savepoint to miejsce do którego transakcja może wrócić jeśli się nie powiedzie

rollback transaction - wycufuje całą tranzakcję
rollback wycofa się do ostatniego savepointa

SAVE TRANSACTION is not supported in distributed transactions started either explicitly with BEGIN DISTRIBUTED TRANSACTION
 or escalated from a local transaction.

transakcja w tle musi być zawsze 'implicite' prawdziwa

UŻYWAMY SAVE TRANSACTIONS żeby osiągnąć efekt NESTED TRANSACTIONS
*/

USE AdventureWorksLT2022

DROP PROCEDURE IF EXISTS SaveTranExample
GO

CREATE PROCEDURE SaveTranExample
AS
BEGIN
-- sprawdzamy czy już jakaś transakcja była uruchomiona
-- przed uruchomieniem funkcji
    DECLARE @TranCounter INT;  
    SET @TranCounter = @@TRANCOUNT;  
    PRINT @@TRANCOUNT
    IF @TranCounter > 0 
        BEGIN
            -- robimy save point, do którego wrócimy jak coś się zepsuje w procedurze
            -- robimy tak tylko jak jest jeszcze inna transakcja w tle
            -- oznacza punkt do którego wrócimy, daje na tą transakcję tag
            SAVE TRANSACTION ProcedureSave
        END
    -- przypadek, gdy to procedura rozpocznie transakcję
    ELSE
        BEGIN
            BEGIN TRANSACTION
        END
    -- próba modyfikacji bazy danych
    BEGIN TRY
        UPDATE SalesLT.Customer SET CustomerID = 2 WHERE CustomerID = 1
        -- jak modyfikacja się uda, to musimy zatwierdzić zmiany dokonane w procedurze
        -- ale NIE zatwierdzamy zmian z poprzedzającej procedurę transakcji
        IF @TranCounter = 0
            BEGIN
                PRINT 'COMMIT for transation if procedure is the only one!'
                COMMIT TRANSACTION
            END
    END TRY
    BEGIN CATCH
        PRINT 'Entered'
        -- jak zmiana się nie powiodła musimy zdecydować jaki rodzaj ROLLBACK wróci nas do 'czasów' sprzed transakcji w procedurze
        IF @TranCounter = 0
            BEGIN
                PRINT 'ROLLBACK for transaction if procedure is the only one!'
                ROLLBACK TRANSACTION -- transakcja z procedura była jedyna, cofamy ją w razie błędu
            END
        ELSE
            BEGIN
                -- jak transkacji się nie da zacomitować, cofamy się do savepoint'a
                BEGIN
                    PRINT 'ROLLBACK to safety'
                    ROLLBACK TRANSACTION ProcedureSave
                END
                IF XACT_STATE() <> -1
                    BEGIN
                        PRINT 'ROLLBACK to safety'
                        ROLLBACK TRANSACTION ProcedureSave
                    END
            END

        -- na końcu wiadomości o błędach
        DECLARE @ErrorMessage NVARCHAR(4000);  
        DECLARE @ErrorSeverity INT;  
        DECLARE @ErrorState INT;  
  
        SELECT @ErrorMessage = ERROR_MESSAGE();  
        SELECT @ErrorSeverity = ERROR_SEVERITY();  
        SELECT @ErrorState = ERROR_STATE();  
  
        RAISERROR (@ErrorMessage, -- Message text.  
                   1, -- Severity.  
                   @ErrorState -- State.  
                   );
    END CATCH
END
GO

UPDATE SalesLT.Customer SET SalesLT.Customer.FirstName='daniel' WHERE SalesLT.Customer.CustomerID = 1
BEGIN TRANSACTION
    UPDATE SalesLT.Customer SET FirstName='anastazy' WHERE CustomerID = 2
    EXEC SaveTranExample
    UPDATE SalesLT.Customer SET FirstName='bartłomiej' WHERE CustomerID = 3
COMMIT TRANSACTION
