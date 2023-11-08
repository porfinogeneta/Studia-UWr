USE AdventureWorksLT2022
GO





-- The deleted table stores copies of the affected rows in the trigger table before they were changed by a DELETE or UPDATE statement 
-- The inserted table stores copies of the new or changed rows after an INSERT or UPDATE statement. During the execution of an INSERT or UPDATE statement


-- robimy trigger, który dla każdej zmiany cen w tabeli Products doda nowy rekord do tabeli ProductCost
DROP TRIGGER IF EXISTS SalesLT.tr_modified_price
GO

CREATE TRIGGER SalesLT.tr_modified_price ON SalesLT.Product AFTER UPDATE, INSERT, DELETE
AS
BEGIN
    -- update
    IF EXISTS (SELECT 1 FROM inserted) AND EXISTS (SELECT 1 FROM deleted)
        BEGIN
            INSERT INTO dbo.ProductCost (ProductID, StandardCost, ListPrice, ModifiedDate)
            SELECT I.ProductID, I.StandardCost, I.ListPrice, I.ModifiedDate
            FROM INSERTED AS I
            INNER JOIN DELETED AS D
            ON I.ProductID = D.ProductID
            WHERE I.StandardCost <> D.StandardCost OR I.ListPrice <> D.ListPrice
        END
    -- insert
    ELSE IF EXISTS (SELECT 1 FROM INSERTED)
        BEGIN
            -- pobieramy tylko te rekordy, które mają inne ProductID od tych obecnych w ProductCost
            -- i dodajemy do ProductCost
            INSERT INTO dbo.ProductCost (ProductID, StandardCost, ListPrice, ModifiedDate)
            SELECT I.ProductID, I.StandardCost, I.ListPrice, I.ModifiedDate
            FROM INSERTED AS I
            LEFT JOIN dbo.ProductCost as PC
            ON I.ProductID = PC.ProductID
            WHERE PC.ProductID IS NULL
        END
    -- delete
    ELSE IF EXISTS (SELECT 1 FROM DELETED)
        BEGIN
            -- dodajemy odpowiedni rekord z polem ModifiedDate = NULL, czyli wiemy że nastąpił koniec zmian
            INSERT INTO dbo.ProductCost (ProductID, StandardCost, ListPrice, ModifiedDate)
            SELECT D.ProductID, D.StandardCost, D.ListPrice, NULL
            FROM deleted AS D
            LEFT JOIN SalesLT.ProducT AS P ON D.ProductID = P.ProductID
            WHERE P.ProductID IS NULL 
        END

    
END
GO

-- UPDATE SalesLT.Product
-- SET StandardCost = 1011.00, ModifiedDate = GETDATE()
-- WHERE ProductID = 680
-- GO

-- INSERT INTO SalesLT.Product
-- VALUES ('TEST1 PRODUCT3', 1004, 'white', 1000.00, 1200.00, 60, 1024.00, 18, 6, '2002-06-01 00:00:00.000', NULL, NULL, NULL, 'no_image_available_small.gif', 'ae638923-2C67-4679-b90e-abbab17dcAaE', '2008-03-11 10:01:36.827')
-- GO

DELETE FROM SalesLT.Product
WHERE SalesLT.Product.ProductID = 680

-- wartości z NULL będą ostatnie, szeregujemy rosnącymi datami, okresy dla cen to poprzednia data, do daty modyfikacji
SELECT * FROM dbo.ProductCost
ORDER BY ProductID, ISNULL(ModifiedDate, '9999-12-31')
GO